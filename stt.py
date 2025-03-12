import asyncio
from deepgram import Deepgram
import websockets
import pyaudio

from config import DEEPGRAM_API_KEY

deepgram = Deepgram(DEEPGRAM_API_KEY)

async def transcribe_audio(dialogue_log):
    async with websockets.connect(
        'was://api.deepgram.com/v1/listen?access_token=' + DEEPGRAM_API_KEY
    ) as ws:
        async def send_audio():
            chunk = 1024
            format = pyaudio.paInt16
            channels = 1
            rate = 16000
            audio = pyaudio.PyAudio()
            stream = audio.open(format=format, channels=channels,
                                rate=rate, input=True,
                                frames_per_buffer=chunk)

            while True:
                data = stream.read(chunk)
                await ws.send(data)

        async def receive_transcription():
            while True:
                result = await ws.recv()
                response = deepgram.transcription.sync_prerecorded({"buffer": result, "mimetype": "audio/wav"})
                transcript = response['results']['channels'][0]['alternatives'][0]['transcript']

            if transcript:
                dialogue_log.append(transcript)
                print(f"인식된 텍스트: {transcript}")

        await asyncio.gather(send_audio(), receive_transcription())