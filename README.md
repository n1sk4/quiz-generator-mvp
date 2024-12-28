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

## Demo
1) Select Question types and output file type: \
   <img src="https://github.com/user-attachments/assets/5eaf1cf3-544c-4f3c-9974-fe83edec423c" alt="drawing" width="300"/>

2) Press Generate Quiz and select a pdf file with relevant data: \
   <img src="https://github.com/user-attachments/assets/a777aa05-b8c6-43ba-add7-4f8a94aebd50" alt="drawing" width="400"/>

3) Generated test (multiple choice): \
   <img src="https://github.com/user-attachments/assets/2f8da1d1-ea45-4f9c-8e66-73323fb905a1" alt="drawing" width="400"/>
