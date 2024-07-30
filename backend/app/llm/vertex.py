import os
import vertexai.preview.generative_models as generative_models
import vertexai
import logging
from vertexai.generative_models import GenerativeModel, Content, Part
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..models.history import History
from .credentials import load_creds

def generate_bot_response(user_message: str) -> str:
    result = ""
    try:
        response = chat.send_message(
            [user_message],
            generation_config=generation_config,
            safety_settings=safety_settings
        )
        logging.info(f"Response: {response}")

        if response and response.candidates:
            result = response.candidates[0]

    except Exception as e:
        logging.error(f"Prediction request failed: {e}")

    return result.text

def get_main_histories_chat() -> list[Content]:
    db: Session = next(get_db())
    db_histories = db.query(History).limit(20).all()

    histories = []
    for db_history in db_histories:
        histories.append(Content(role="user", parts=[Part.from_text(str(db_history.user_message))]))
        histories.append(Content(role="model", parts=[Part.from_text(str(db_history.bot_response))]))

    return histories

# Set up logging
logging.basicConfig(level=logging.INFO)

credentials = load_creds()

PROJECT_ID = os.getenv("PROJECT_ID")
ENDPOINT_ID = os.getenv("ENDPOINT_ID")
REGION = os.getenv("REGION")

vertexai.init(project=PROJECT_ID, location=REGION, credentials=credentials)
vertex_endpoint = f'projects/{PROJECT_ID}/locations/{REGION}/endpoints/{ENDPOINT_ID}'
model = GenerativeModel(
    vertex_endpoint,
)

chat_history = get_main_histories_chat()
chat = model.start_chat(history=chat_history)

generation_config = {
    "max_output_tokens": 2048,
    "temperature": 1,
    "top_p": 1,
}

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}