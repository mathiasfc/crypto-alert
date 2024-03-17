import telegram
import config


async def send_message(message):
    bot = telegram.Bot(config.telegram_bot_api_key)
    try:
        await bot.send_message(
            text=message,
            chat_id=config.telegram_chat_id,
            parse_mode=telegram.constants.ParseMode.HTML,
        )
    except Exception as e:
        print(f"An error occurred: {e}")
