import openai
from config import OPENAI_API_KEY

def generate_summary(dialogue_log):
    text = "\n".join(dialogue_log)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= [
            {"role": "system", "content": "상담 기록 요약"},
            {"role": "user", "content": text}
        ]
    )

    return response['choices'][0]['message']['content']