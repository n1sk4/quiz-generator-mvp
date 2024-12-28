# Quiz generator
Example project for generating Quiz questions using LLM API.

## Setup LLM API
This project uses Open AI LLM API:
[OpenAI API documentation](https://platform.openai.com/docs/overview)

Following the Quickstart setup the prompt, model, etc...

## Setup Python app
Windows setup (Python and pip already installed):
```sh
pip install --upgrade pip

pip install venv 

python -m venv %path\project_name%

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser # if needed

Scripts\activate.ps1 # for Powershell or
Scripts\activate.bat # cmd

pip install openai # Open AI lib

pip install pymupdf # PDF read/write lib

pip install dotenv # environment variables (for API keys) lib
```

Create .env file
```
LLM_API_KEY = "your API key" 
ORG_ID = "your organization ID"
PROJECT_ID = "your project ID"
```

Run the app:
```sh
python app.py
```