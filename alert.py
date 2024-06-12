import asyncio
import config
import requests
from telegram_bot import send_message

previous_crypto_slug = None
previous_price_change_1h = None


def fetch_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def extract_first_gainer(data):
    if data and isinstance(data, dict) and "data" in data:
        gainer_list = data["data"].get("gainerList")
        if gainer_list and isinstance(gainer_list, list) and len(gainer_list) > 0:
            first_gainer = gainer_list[0]

            return first_gainer

        else:
            print("No gainer list found or empty gainer list.")
    else:
        print("Invalid data format or 'data' key not found.")

    return None


def extract_price_change(first_gainer):
    if "priceChange" in first_gainer and isinstance(first_gainer["priceChange"], dict):
        price_change_1h = first_gainer["priceChange"].get("priceChange1h")

        if price_change_1h is not None:
            return price_change_1h
        else:
            print("Price change (1 hour) not found in the first gainer.")
    else:
        print("Invalid price change data for the first gainer.")

    return None


def extract_current_price(first_gainer):
    if "priceChange" in first_gainer and isinstance(first_gainer["priceChange"], dict):
        current_price = first_gainer["priceChange"].get("price")

        if current_price is not None:
            return current_price
        else:
            print("Current price not found in the first gainer.")
    else:
        print("Invalid price change data for the first gainer.")

    return None


async def check_prev_and_curr_price_change(endpoint):
    # Access the global variables
    global previous_crypto_slug
    global previous_price_change_1h

    while True:

        # Fetch data from the endpoint
        data = fetch_data(endpoint)

        # Extract value from the response
        first_gainer = extract_first_gainer(data)

        if first_gainer is not None:
            # Extract value from the response
            current_coin_price = extract_current_price(first_gainer)
            current_price_change_1h = extract_price_change(first_gainer)
            current_crypto_slug = first_gainer["slug"]

            # Check if there is a previous value
            if previous_price_change_1h is not None:
                prev_value = float(previous_price_change_1h)
                curr_value = float(current_price_change_1h)

                # Calculate the difference between the current and previous values
                difference = abs(current_price_change_1h - previous_price_change_1h)

                log_message = f"{first_gainer['name']} ({first_gainer['symbol']})\n- Prev: {prev_value:.2f}% ({previous_crypto_slug})\n- Curr: {curr_value:.2f}% ({current_crypto_slug})\n- Diff: {difference:.2f}%\n\n"
                print(log_message)

                # Check if the difference between the previous and the current value, to send the telegram message
                if (
                    difference > config.difference_to_alert
                    and previous_crypto_slug == current_crypto_slug
                ):
                    # Only send the message if the difference is positive
                    if current_price_change_1h > previous_price_change_1h:
                        html_log_message = f"🟢 {first_gainer['name']} (<b>{first_gainer['symbol']}</b>)\n\n - <b>Previous</b>: {prev_value:.2f}%\n - <b>Current</b>: {curr_value:.2f}% \n\n Difference: + {difference:.2f}%\n Price: {current_coin_price:.2f} USD\n\n <a href='https://coinmarketcap.com/gainers-losers/' target='_blank'>View on coinmarketcap</a>"
                        await send_message(html_log_message)

            # Store the current value
            previous_price_change_1h = current_price_change_1h
            previous_crypto_slug = first_gainer["slug"]

        await asyncio.sleep(config.interval)
