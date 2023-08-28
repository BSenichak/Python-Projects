import AI
messages = AI.set_ai_role()  # задаємо характер інтеллекту
while True:
    user_message = AI.get_user_input()  # Отримуємо запит (prompt) користувача
    AI.add_message(messages, "user", user_message)  # Додаємо запит до всіх попередніх запитів (Для того щоб АІ знав що було написано раніше)
    response = AI.generate(messages)  # Отримуємо відповідь від АІ
    print('ChatGPT: ')  # Щоб було видно що це відповідь від GPT
    AI.get_response(response)
    AI.add_message(messages, "assistant", response)  # додаємо відповідь АІ до всіх повідомлень