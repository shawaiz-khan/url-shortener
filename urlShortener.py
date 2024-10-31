import string
import random

url_id = 0
url_ls = []


def generate_id():
    global url_id
    url_id += 1
    return url_id


class url_shortener:
    def __init__(self):
        self.long_url = {}
        self.short_url = {}
        print(f"URL SHORTENER")

    def get_url(self):
        user_url = input("Enter a URL: ")
        generate_id()
        self.long_url[url_id] = {"url": user_url}

    def shorten_url(self):
        for _ in range(10):
            val = random.choice(string.ascii_letters + string.digits)
            global url_ls
            url_ls.append(val)

    def add_short_url(self):
        global url_ls
        newRes = "".join(url_ls) + ".xyz"
        self.short_url[url_id] = {"shortURL": newRes}
        print(self.short_url, newRes)

Object = url_shortener()
newURL = Object.shorten_url()
newURL = Object.add_short_url()