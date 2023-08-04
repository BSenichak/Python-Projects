import openai

api_key = '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'
openai.api_key = api_key

def get_gpt3_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        stop=None,
        temperature=0.7,
        n=1
    )
    return response['choices'][0]['text'].strip()

def main():
    print("Привіт! Чим я можу допомогти?")
    chat_history = ""

    while True:
        user_input = input("Ти: ")

        if user_input.lower() == 'вийти':
            print("До побачення!")
            break

        chat_history += f"Ти: {user_input}\n"
        response = get_gpt3_response(chat_history)
        chat_history += f"Бот: {response}\n"
        print(f"Бот: {response}")

if __name__ == "__main__":
    main()

