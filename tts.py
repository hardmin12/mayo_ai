from google.cloud import texttospeech

client = texttospeech.TextToSpeechClient()

def synthesize_speech(text):
    input_text = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="ko-KR",
        name="ko-KR-Wavenet-A"
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16
    )

    response = client.synthesize_speech(
        input=input_text, voice=voice, audio_config=audio_config
    )

    with open("output.wav", "wb") as out:
        out.write(response.audio_content)

        print("음성 파일 생성 완료!")

        import simpleaudio as sa
        wave_obj = sa.WaveObject.from_wave_file("output.wav")
        play_obj = sa.play()
        play_obj.wait_done()