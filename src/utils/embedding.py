import os
import requests
from dotenv import load_dotenv

load_dotenv()

def embedd(query:str):
    model_id = os.getenv("MODEL_ID")
    hf_token = os.getenv("HF_API_KEY")
    hf_url = os.getenv("API_URL").format(MODEL_ID=model_id)

    headers = {
        "Authorization" : f"Bearer {hf_token}",
        "Content-Type": "application/json",
        "X-Wait-For-Model": "true" # Forces the API to load the model if it's idle
    }

    #hugging face format to send query
    payload = {
        "inputs": query
        # "options": {"wait_for_model": True}
    }

    response = requests.post(
        hf_url,
        headers=headers,
        json=payload
    )

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code} : {response.text}")
        return None
    