# src/core/xai_client.py
import os
from xai_sdk import Client
from xai_sdk.chat import user, system

def get_xai_client():
    api_key = os.getenv("XAI_API_KEY")
    if not api_key:
        raise ValueError("XAI_API_KEY environment variable not set")
    return Client(api_key=api_key)

def create_chat(model="grok-4-1-fast-reasoning", system_prompt=None):
    client = get_xai_client()
    chat = client.chat.create(model=model)
    if system_prompt:
        chat.append(system(system_prompt))
    return chat

# Quick test
if __name__ == "__main__":
    chat = create_chat(system_prompt="You are Grok. Be concise and truthful.")
    chat.append(user("Say hello in one word."))
    response = chat.sample()
    print(response.content)
