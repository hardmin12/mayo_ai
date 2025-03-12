import asyncio
from stt import transcribe_audio
from nlp import generate_response
from tts import synthesize_speech
from summary import generate_summary

dialogue_log = []

async def main():
    try:
        await transcribe_audio(dialogue_log)
    finally:
        print("\n 상담 종료!")
        summary = generate_summary(dialogue_log)
        print(f"\n 상담 요약:\n{summary}")

if __name__ == "__main__":
    asyncio.run(main())