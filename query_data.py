import os
import argparse
import time
from langchain_chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.gpt4all import GPT4All

from get_embedding_function import get_embedding_function
from dotenv import load_dotenv

load_dotenv()

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""


def main():
    # Create CLI.
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text
    query_rag(query_text)


def query_rag(query_text: str):
    # Prepare the DB.
    embedding_function = get_embedding_function()
    db = Chroma(
        persist_directory=os.getenv("CHROMA_PATH"),
        embedding_function=embedding_function,
    )

    # Search the DB.
    results = db.similarity_search_with_score(query_text, k=5)

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    # print(prompt)

    model = GPT4All(model=os.getenv("MODEL_PATH"))

    # measure time of running the model
    start_time = time.time()
    # Invoke the model with the prompt
    response_text = model.invoke(prompt)
    end_time = time.time()

    print(f"Model response time: {end_time - start_time:.2f} seconds")

    # sources = [doc.metadata.get("id", None) for doc, _score in results]
    # formatted_response = f"Response: {response_text}\nSources: {sources}"
    # print(formatted_response)
    print(f"{response_text}\n")
    return response_text


if __name__ == "__main__":
    main()
