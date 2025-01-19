import openai
from openai import OpenAI

def gpt_message(message):
    client = OpenAI()
    # TEST
    # print(f"API Key: {openai.api_key}")

    response_text = ""

    completion = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": message}],
        stream=True,
    )

    for chunk in completion:
        delta_content = chunk.choices[0].delta.content
        if delta_content is not None:
            response_text += delta_content
            print(delta_content, end="")

    return response_text
