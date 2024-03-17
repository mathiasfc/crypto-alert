<!-- Centered Image -->
<p align="center">
  <img src="images/crypto-alert-bot-avatar.png" alt="Crypto Alert Bot Avatar" width="200px">
</p>

# Crypto Alert Bot

Welcome to Crypto Alert Bot! This repository contains code for a Telegram bot designed to alert users when a cryptocurrency experiences a significant increase in price. This README provides an overview of the bot's functionality, how to set it up, and future plans for development.

## Summary

1. [Functionality](#functionality)
2. [How to Use](#how-to-use)
3. [Configure Settings](#configure-settings)
4. [Where to Run My Bot?](#where-to-run-my-bot)
5. [Live Example](#live-example)
6. [Future Development](#future-development)
7. [Contributing](#contributing)
8. [Disclaimer](#disclaimer)

## Functionality

The Crypto Alert Bot monitors the price of cryptocurrencies at regular intervals and sends alerts to a designated Telegram group when the price of a selected cryptocurrency rises sharply.

Currently, the bot is configured to detect a price increase of 5% within the last hour. It checks for price changes every 10 minutes and sends a notification to the Telegram group if the criteria are met.

You can set your own parameters for the bot at `config.py`

## How to Use

To use the Crypto Alert Bot, follow these steps:

1. **Clone the Repository**: Clone this GitHub repository to your local machine.

   ```
   git clone https://github.com/your-username/crypto-alert-bot.git
   ```

2. **Set Up Telegram Bot**:

   - Create a new bot on Telegram using BotFather and obtain the API token. You can follow the official Telegram documentation to [obtain your bot token](https://core.telegram.org/bots/tutorial#obtain-your-bot-token).
   - Obtain the Telegram Chat ID where you want to receive alerts. You can find instructions on how to obtain the chat ID [here](https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id).
   - Rename the `.env.example` file to `.env` and fill it with the obtained values:
     ```
     TELEGRAM_API_TOKEN=your_bot_token_here
     TELEGRAM_CHAT_ID=your_chat_id_here
     ```

3. **Configure Settings**:

   - Open the `config.py` file located in the project directory.
   - Below is an explanation of each configurable parameter:

     - `interval`: This parameter determines the interval in seconds at which the bot checks for price changes. By default, it is set to 600 seconds (10 minutes). You can modify this value to adjust how frequently the bot checks for price updates.

     - `difference_to_alert`: This parameter defines the percentage difference between the previous and current price of a cryptocurrency. If the difference exceeds this threshold, the bot sends a notification to the Telegram group. The default value is 5%, but you can modify it based on your desired sensitivity to price changes.

4. **Install Dependencies**: Install the required Python dependencies using pip.

   ```
   pip install -r requirements.txt
   ```

   ⚠️ _python 3.8 or higher is required_

5. **Run the Bot**: Execute the main Python script to start the bot.

   ```
   python main.py
   ```

## Where to Run My Bot?

You have the option to run the Crypto Alert Bot either locally or on a hosting service that supports Python, such as [PythonAnywhere](https://www.pythonanywhere.com/).

## Live Example

To see the Crypto Alert Bot in action, you can join the Telegram group where the bot is actively running and sending alerts:

[Join Telegram Group](https://t.me/+i_Kpt2lTGmQ3MTRh)

In this group, you'll receive real-time notifications whenever the bot detects a significant price increase in a cryptocurrency. It's a great way to experience firsthand how the bot operates and the type of alerts it provides.

## Future Development

In the future, we plan to expand the functionality of the Crypto Alert Bot to include:

- Customizable alert thresholds: Allow users to set their desired percentage increase for alerts.
- Additional platforms: Extend the bot's capabilities to other messaging platforms beyond Telegram.
- Enhanced analysis: Implement more sophisticated analysis techniques to identify potentially lucrative cryptocurrency investments.
- User interaction: Allow users to interact with the bot to request specific information or perform actions.

## Contributing

Contributions to the Crypto Alert Bot are welcome! If you have any ideas for improvements or new features, please open an issue or submit a pull request ☕

## Disclaimer

Please note that cryptocurrency trading carries inherent risks, and the Crypto Alert Bot is provided for informational purposes only. The bot's alerts should not be considered financial advice, and users should conduct their own research before making any investment decisions.

Happy trading!
