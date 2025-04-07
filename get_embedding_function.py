import os
from langchain_community.embeddings.gpt4all import GPT4AllEmbeddings
# from langchain_community.embeddings.bedrock import BedrockEmbeddings


def get_embedding_function():
    # embeddings = BedrockEmbeddings(credentials_profile_name="default", region_name="us-east-1")
    embeddings = GPT4AllEmbeddings(model=os.getenv("MODEL_PATH"))
    return embeddings
