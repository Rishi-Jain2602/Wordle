import requests
from dotenv import load_dotenv
load_dotenv()
import os
Hugging_API = os.environ['Huggingface_API_Token']

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
headers = {"Authorization": f"Bearer {Hugging_API}"}

def description(text):
	payload = {"inputs":f"what is {text}. Answer briefly"}
	response = requests.post(API_URL, headers=headers, json=payload)
	output =  response.json()
	return output[0]['generated_text']
