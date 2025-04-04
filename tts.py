import requests
import os
import base64
import json
def text_to_speech(input_text):
    url = "https://api.sarvam.ai/text-to-speech"

    payload = {
        "inputs": [input_text],
        "target_language_code": "te-IN",
        "speaker": "meera",
        "pitch": -0.75,
        "enable_preprocessing": True,
        "model": "bulbul:v1",
        "eng_interpolation_wt": 0.4
    }

    headers = {
        "api-subscription-key": "",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    response_dict = json.loads(response.text)

    try:
        base64_audio = response_dict["audios"][0]
    except (KeyError, IndexError) as e:
        print(f"Error extracting audio: {e}")
        return None

    if "," in base64_audio:
        base64_audio = base64_audio.split(",")[1]

    try:
        audio_data = base64.b64decode(base64_audio)
    except Exception as e:
        print(f"Base64 decode failed: {e}")
        return None

    output_dir = "/home/ubuntu/neuraoak/sarvam_ai_files"
    os.makedirs(output_dir, exist_ok=True)

    audio_file_path = os.path.join(output_dir, "output_audio.wav")

    try:
        with open(audio_file_path, "wb") as audio_file:
            audio_file.write(audio_data)
        print(f"✅ Audio saved to: {audio_file_path}")
        return audio_file_path
    except Exception as e:
        print(f"File write failed: {e}")
        return None
