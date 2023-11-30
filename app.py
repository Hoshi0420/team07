from crawler.ff import *
from DB.to_db import insert_db
import requests as rq


def main() -> None:
    url: str = 'http://icanhazip.com/'

    proxies: dict[str,str] = {
        'http': 'socks5://127.0.0.1:9050',
        'https': 'socks5://127.0.0.1:9050'
    }

    response : rq.Response = rq.get(url=url,proxies=proxies)
    print(response.text)


if __name__ == "__main__":
    try:
        main()
        bot = YouTubeBot()
        result_df = bot.run()  # Save the returned DataFrame as a variable
        bot.cleanup()
        table_name = 'crawl'
        insert_db(df=result_df, table_name=table_name)
        print("Script executed successfully.")

    except YouTubeBotError as e:
        print(f"Custom error raised: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
