# AI-Agent for Bid Processes

## Status

The project is at it's first stage and more a collection of code-snippets, than a regular project.
Credits to https://github.com/pixegami

## Overview

This project is an AI-powered agent designed to streamline and enhance the bid processes around an OPLs client. By leveraging advanced natural language processing and automation, the AI-agent extracts information from documents, processes it intelligently, and performs various tasks to support the bid-workflow.

## Features

- **Document Extraction**: Automatically extracts content from bid-related documents.
- **Chunking and Embedding**: Splits documents into manageable chunks and generates embeddings for efficient information retrieval.
- **LLM Integration**: Feeds processed data into a large language model (LLM) to retrieve relevant information and insights.
- **Task Automation**:
    - Prepares ESR-slides based on extracted data
    - Schedules and invites stakeholders to ESR- and SSR-meetings
    - Creates and updates CRM entry automatically
    - Creates Talento-opportunity to search for partners to staff the project-team
    - Start DRSR-request automatically

## Benefits

- Saves time by automating repetitive tasks
- Improves accuracy in bid preparation and management
- Enhances collaboration and decision-making with timely insights
- Reduces manual effort, allowing you to focus on strategic activities

## Getting Started

1. Clone the repository:
     ```bash
     git clone https://github.com/your-username/ai-agent.git
     ```

2. Create environment:

     SHIFT+CRTL+P - Python-Create Envrionment (including pip-install of requirements.txt)
     Open up a terminal 
     ```bash
     .\.venv\Scripts\activate.ps1
     ```

3. optional install of dependencies (if not done in step 2):
     ```bash
     pip install -r requirements.txt
     ```

4. Provide an OpenAI-API-key (optional)
     create a file '.env' within the root-directory (contained within .gitignore)
     provide the key-variable OPENAI_API_KEY = "your-key" if OpenAI is used as LLM

5. Define the language-model
     Place your model within ./models and 

5. Run the application:
     ```bash
     python extract_zip.py
     python populate_database.py --reset
     python query_data.py "What is the project name?"
     ```

## Technologies Used

- Python
- Natural Language Processing (NLP)
- Large Language Models (LLMs)
- Embedding generation libraries
- Task automation frameworks

![LLM-stages as of anthropic.com](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F7418719e3dab222dccb379b8879e1dc08ad34c78-2401x1000.png&w=3840&q=75)

## VSCode Extensions

Atom One Dark Theme, Better Comments, Django, GitHub Copilot, GitHub Pull Requests, IntelliCode, Jupyter, Material Icon Theme, Material Theme Icons, Path Intellisense, Python,
Python Debugger, Python Environment Manager, Python Environments, Python Extension Pack, Python Intend, Pylance, Ruff, vscode-pdf

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions or support, please contact [steve.baumann@cgi.com].
