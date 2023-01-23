import openai
from _vars import openai_token

openai.api_key=openai_token

def gpt3_msg(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=256,
        top_p=1.0,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response