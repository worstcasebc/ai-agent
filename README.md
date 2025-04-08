# AI-Agent for Bid Processes

## Status

The project is at it's first stage and more a collection of code-snippets, than a regular project.
Credits to https://github.com/pixegami

## Overview

This project is an AI-powered agent designed to streamline and enhance the bid processes around an OPLs client. By leveraging advanced natural language processing and automation, the AI-agent extracts information from documents, processes it intelligently, and performs various tasks to support the bid-workflow.

## Features

- &#9989; **Document Extraction**: Automatically extracts content from bid-related documents.
- &#9989; **Chunking and Embedding**: Splits documents into manageable chunks and generates embeddings for efficient information retrieval.
- &#9989; **LLM Integration**: Feeds processed data into a large language model (LLM) to retrieve relevant information and insights.
- &#10060; **Task Automation**:
    - Prepares ESR-slides based on extracted data
    - Schedules and invites stakeholders to ESR- and SSR-meetings
    - Creates and updates CRM entry automatically
    - Creates Talento-opportunity to search for partners to staff the project-team
    - Start DRSR-request automatically
    - Find and retrieve project-references from BidGen and/or BDKX
    - Create concepts and other requested documents

## Benefits

- Saves time by automating repetitive tasks
- Improves accuracy in bid preparation and management
- Enhances collaboration and decision-making with timely insights
- Reduces manual effort, allowing you to focus on strategic activities

## Getting Started

1. Clone the repository:
     ```bash
     git clone https://github.com/worstcasebc/ai-agent.git
     ```

2. change directory
     ```bash
     cd ai-agent
     ```

3. Create environment:
     ```bash
     python -m venv .venv
     ```

4. Activate environment
     
     If powershell is used
     ```bash
     .\.venv\Scripts\activate.ps1
     ```
     In case of terminal-window
     ```bash
     .\.venv\Scripts\activate.bat
     ```
5. Installation of dependencies:
     ```bash
     pip install -r requirements.txt
     ```

6. set-up for your environment

     copy '.env.example' into '.env' and update with your paths

7. Define the language-model

     Place your model within ./models and update the .env-variable (Download-link below)
     
     Tested with

     [Orca-2-13B](https://huggingface.co/TheBloke/Orca-2-13B-GGUF/blob/main/orca-2-13b.Q4_0.gguf)

     [Meta-Llama-3-8B](https://huggingface.co/QuantFactory/Meta-Llama-3-8B-Instruct-GGUF/blob/main/Meta-Llama-3-8B-Instruct.Q4_0.gguf)

8. Run the application:
     ```bash
     python extract_zip.py
     ```
     ```bash
     python populate_database.py --reset
     ```
     ```bash
     python query_data.py "What is the name of the project?"
     ```

## Technologies Used

- Python
- Natural Language Processing (NLP)
- Large Language Models (LLMs)
- Embedding generation libraries
- Task automation frameworks

![LLM-stages as of anthropic.com](https://www-cdn.anthropic.com/images/4zrzovbb/website/7418719e3dab222dccb379b8879e1dc08ad34c78-2401x1000.png)

## recommended VSCode Extensions

Atom One Dark Theme, Better Comments, Django, GitHub Copilot, GitHub Pull Requests, IntelliCode, Jupyter, Material Icon Theme, Material Theme Icons, Path Intellisense, Python,
Python Debugger, Python Environment Manager, Python Environments, Python Extension Pack, Python Intend, Pylance, Ruff, vscode-pdf

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions or support, please contact [steve.baumann@cgi.com].
