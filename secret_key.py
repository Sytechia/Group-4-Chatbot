from openai import OpenAI
import os

openai_api_key = "YOUR OPENOI API KEY"

#add secret key here
client = OpenAI(api_key=openai_api_key)

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'supersecretkey'
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'pdf', 'docx'}

    # OpenAI API Key (set your OpenAI API key here or through environment variable)
    OPENAI_API_KEY = os.environ.get(openai_api_key) or openai_api_key