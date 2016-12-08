import requests
from client import BaseClient
from datetime import date
from _overlapped import NULL


def get_age(birthday):
    today = date.today()
    age = today.year - int(birthday[2], base=10)
    if today.month < int(birthday[1], base=10):
        age -= 1
    elif today.month == int(birthday[2], base=10) and today.day < int(birthday[0], base=10):
        age -= 1
    return age


class GetUser(BaseClient):
    BASE_URL = 'https://api.vk.com/method/'
    method = 'users.get'

    def __init__(self, name):
        self.username = name

    def get_params(self):
        return {
            'user_ids': self.username
        }


class GetFriends(BaseClient):
    BASE_URL = 'https://api.vk.com/method/'
    method = 'friends.get'

    def __init__(self, user_id):
        self.user_id = user_id

    def get_params(self):
        return {
            'user_id': self.user_id,
            'fields': 'bdate'
        }
