import openai
from dotenv import load_dotenv
import os

# Load environment variables and set API key
load_dotenv()
openai.api_key = os.getenv("OPEN_AI_API_KEY")

def upload_file():
    try:
        with open("info.txt", "rb") as file:
            response = openai.File.create(file=file, purpose="fine-tuning")
        return response["id"]
    except:
        print("Error")
    

def create_assistant(file):
    assistant = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful bot to help users check-in in an Airbnb listed property."
                
            }
        ],
    )
    return assistant

# Main flow
file_id = upload_file()
assistant = create_assistant(file_id)
print(assistant)