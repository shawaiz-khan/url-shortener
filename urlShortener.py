import string
import random

url_id = 0
url_mapping = {}


def generate_id():
    global url_id
    url_id += 1
    return url_id


class URLShortener:
    def __init__(self):
        print("URL SHORTENER")

    def generate_short_code(self, length=6):
        return "".join(random.choices(string.ascii_letters + string.digits, k=length))

    def shorten_url(self, long_url):
        global url_mapping
        unique_id = generate_id()
        short_code = self.generate_short_code()
        short_url = f"{short_code}.xyz"

        url_mapping[short_url] = {"long_url": long_url, "id": unique_id}

        return short_url

    def get_url(self):
        user_url = input("Enter a URL to shorten: ")
        short_url = self.shorten_url(user_url)
        print(f"Shortened URL: {short_url}")
        return user_url, short_url

    def retrieve_url(self, short_url):
        if short_url in url_mapping:
            return url_mapping[short_url]["long_url"]
        else:
            return "URL not found."


url_shortener = URLShortener()
long_url, short_url = url_shortener.get_url()

retrieved_url = url_shortener.retrieve_url(short_url)
print(f"Original URL: {retrieved_url}")