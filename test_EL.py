import requests
import os


parent_folder = os.path.dirname(__file__)
root_folder = os.path.dirname(parent_folder)
save_path = os.path.join(parent_folder, 'output.mp3')

key: str
with open(os.path.join(root_folder, 'EL_key.txt'), 'r') as file:
    key = file.read()

CHUNK_SIZE = 1024
# url = "https://api.elevenlabs.io/v1/text-to-speech/<voice-id>"
url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"

headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": key
}

data = {
    "text": """School sucks ass""",
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
        "stability": 0.0,
        "similarity_boost": 0.5
    }
}

response = requests.post(url, json=data, headers=headers)
with open(save_path, 'wb') as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)

print("END")
