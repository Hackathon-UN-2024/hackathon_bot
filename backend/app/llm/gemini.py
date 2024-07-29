import os
import google.generativeai as genai
from google.oauth2 import service_account

service_account_file = './configs/client_secret.json'

# Authenticate using the service account
credentials = service_account.Credentials.from_service_account_file(service_account_file)
genai.configure(credentials=credentials)

model_name = os.getenv("TUNED_MODEL")

def generate_bot_response(user_message: str) -> str:
    tuned_model = genai.GenerativeModel(model_name=f'tunedModels/{model_name}')
    result = tuned_model.generate_content(user_message)

    return result.text
