import openai
import time

openai.api_key = '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'

def get_response(response):
    for i in range(len(response)):  # Друкуємо по одній букві ніби це хтось пише
        print(response[i], end='')
        time.sleep(0.2)

def set_ai_role():
    startprompt = input("Input AI Character:\n")
    return [
        {"role": "system", "content": startprompt},
    ]


def get_user_input():
    print("\n")
    return input("User: ")


def add_message(messages, role, content):
    messages.append({"role": role, "content": content})


def generate(messages):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        messages=messages
    )
    return completion.choices[0].message.content

