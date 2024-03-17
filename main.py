import asyncio
from alert import check_prev_and_curr_price_change


async def main():
    endpoint = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/spotlight?rankRange=100&timeframe=1h&dataType=2&limit=5"
    await check_prev_and_curr_price_change(endpoint)


if __name__ == "__main__":
    asyncio.run(main())
