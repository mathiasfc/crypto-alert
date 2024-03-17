from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Interval to check in seconds (600 = 10 minutes)
interval = 600

# The difference (%) between the previous and the current value
# If the difference is greater than this parameter, send the telegram message
difference_to_alert = 5

# Telegram bot API key
telegram_bot_api_key = os.getenv("TELEGRAM_BOT_API_KEY")

# Telegram chat ID
telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")
