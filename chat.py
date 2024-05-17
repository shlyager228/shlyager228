from telethon import TelegramClient
import time

# Ваши учетные данные для Телеграма
api_id = '29366791'
api_hash = '46e455dccba096e2da7ac8a173ee8ce8'
phone = '+79161583412'

# Создание клиента
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone)

    # Список ID чатов и ID сообщения для пересылки
    chat_ids = [ '@dpdpdhsjsbsbsb', '@toncheckschat', '@crypto_reklama', '@Xrokettontop', '@AliensAirDropClubchat', '@reklama_refok', '@contchek', '@Active_checks_chat', "@pr_chat" ]  # Замените на реальные ID чатов
    message_link = 't.me/c/2096010316/2550'  # Ссылка на сообщение для пересылки

    # Извлечение информации о сообщении из ссылки
    parts = message_link.split('/')
    try:
        message_chat_id = int(parts[-2])
        message_id = int(parts[-1])
    except ValueError:
        print("Ошибка: Неверный формат ссылки на сообщение.")
        return

    try:
        # Получение сущности чата с сообщением
        from_peer = await client.get_entity(message_chat_id)
    except Exception as e:
        print(f"Ошибка при получении сущности чата: {e}")
        return

    while True:  # Бесконечный цикл
        for chat_id in chat_ids:
            try:
                await client.forward_messages(chat_id, message_id, from_peer)
                print(f'Сообщение переслано в {chat_id}')
            except Exception as e:
                print(f"Ошибка при пересылке сообщения в {chat_id}: {e}")

        # Интервал между всей рассылкой
        time.sleep(400)  # Интервал в секундах (например, 600 секунд = 10 минут)

with client:
    client.loop.run_until_complete(main())



