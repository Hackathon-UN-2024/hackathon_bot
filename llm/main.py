import os
import time
import google.generativeai as genai
from core.database import get_db
from sqlalchemy.orm import Session
from models.history import History

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

model_name = os.getenv("TUNED_MODEL")

def training_data():
    db: Session = get_db()
    histories = db.query(History).all()

    data = []
    for history in histories:
        data.append({"input": history.user_message, "output": history.bot_response})

    return data

def train_model():
    # Create a tuned model
    operation = genai.create_tuned_model(
        source_model="models/gemini-1.0-pro-001",
        training_data=training_data(),
        id = f'tunedModels/{model_name}',
        epoch_count = 100,
        batch_size=4,
        learning_rate=0.001,
    )

    for _ in operation.wait_bar():
        time.sleep(5)

def main():
    tuned_models = genai.list_tuned_models()
    if model_name is not None and model_name not in tuned_models:
        train_model()

if __name__ == "__main__":
    main()