from fastapi import FastAPI, Form
import httpx  
from fastapi.responses import PlainTextResponse
import stt
import query_retrieval
import tts

app = FastAPI()

FILE_NAME = "/home/ubuntu/neuraoak/latest_recording.wav"

@app.get("/twiml-response")
async def twiml_response():
    """ TwiML response for Twilio call recording """
    twiml = """<?xml version="1.0" encoding="UTF-8"?>
    <Response>
        <Say>Welcome to our insurance support. Please ask your question after the beep.</Say>
        <Record
            action="https://7b87-13-202-216-63.ngrok-free.app/twilio-webhook"
            method="POST"
            maxLength="500"
            playBeep="true"
            trim="trim-silence"
            finishOnKey="*"
        />
    </Response>"""
    return PlainTextResponse(twiml, media_type="text/xml")

@app.post("/twilio-webhook")
async def save_recording(RecordingUrl: str = Form(...)):
    """ Download & Save Twilio Recording """
    async with httpx.AsyncClient() as client:
        import time
        time.sleep(3)
        response = await client.get(RecordingUrl + ".wav")
        time.sleep(3)
        print(response)
        with open(FILE_NAME, "wb") as f:
            f.write(response.content)
        transcript = stt.stt()
        rag_out = query_retrieval.retrieval(transcript) # our RAG process
        tts.text_to_speech(rag_out)
        
        return PlainTextResponse("<Response><Say>Thank you! have a good day</Say></Response>", media_type="text/xml")