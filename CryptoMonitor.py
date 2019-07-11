# importing the requests library
import os
import time
import requests
from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen
import argparse
import platform


def show(args, a):
    start_time = time.time()

    # api-endpoint
    url = "https://api.independentreserve.com/Public/GetMarketSummary?"
    params = {'primaryCurrencyCode': args.crypto, 'secondaryCurrencyCode': args.fiat}

    while True:
        r = requests.get(url=url, params=params)
        # extracting data in json format
        data = r.json()

        # extracting data
        last_price = data['LastPrice']
        market_buy = data['CurrentHighestBidPrice']
        market_sell = data['CurrentLowestOfferPrice']

        # some variables
        current_value = float(last_price * args.amount)
        profit = current_value - args.price

        # extracting news
        news_url = "https://news.google.com/rss/search?q=bitcoin&hl=en-AU&gl=AU&ceid=AU:en"
        client = urlopen(news_url)
        xml_page = client.read()
        client.close()

        soup_page = Soup(xml_page, "xml")
        news_list = soup_page.findAll("item")

        # Labels
        profits_label = "PROFITS"
        centered_profits = profits_label.center(50)
        bitcoin_label = "CRYPTO PRICES"
        centered_bitcoin = bitcoin_label.center(50)
        news_label = "LATEST NEWS"
        centered_news = news_label.center(50)

        if a == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

        print("-" * 49)
        print(centered_bitcoin)
        print("-" * 49)
        print("Last Price: $%s" % last_price)
        print("Highest Buyer price: $%s" % market_buy)
        print("Lowest Seller Price: $%s" % market_sell)
        print("-" * 49)
        print(centered_profits)
        print("-" * 49)
        print("Amount invested: $%s" % args.price)
        print("Current Value: $%.2f" % current_value)
        print("Profit: $%.2f" % profit)
        print("Return on Investment: %.2f" % (((current_value - args.price) / args.price) * 100), "%")
        print("-" * 49)
        print(centered_news)
        print("-" * 49)


        for i in range(4):
            print(news_list[i].title.text)
            print("-" * 49)

        time.sleep(1.0 - ((time.time() - start_time) % 1.0))


def main():
    parser = argparse.ArgumentParser(description='Bitcoin Dashboard. \n Example: CryptoMonitor.py -f aud -c xbt -a '
                                                 '0.052 -p 650')
    parser.add_argument("-f", "--fiat", help="The Fiat Currency Code you want to use.", type=str, required=True)
    parser.add_argument("-c", "--crypto", help="The CryptoCurrency Code you want to use", type=str, required=True)
    parser.add_argument("-a", "--amount", help="The amount of bitcoin you own", type=float, required=True)
    parser.add_argument("-p", "--price", help="The Price paid for that amount of CryptoCurrency (before exchange fees)",
                        type=float, required=True)
    args = parser.parse_args()
    a = platform.system()
    show(args, a)


if __name__ == '__main__':
    main()
