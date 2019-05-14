import flask
from telebot import types
from config import *
from NazzmorgRus import new_echo_bot
import os

server = flask.Flask(__name__)


@server.route(methods=['POST'])
def get_message():
    new_echo_bot.process_new_updates([types.Update.de_json(
        flask.request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route(methods=['GET'])
def index():
    new_echo_bot.remove_webhook()
    new_echo_bot.set_webhook(url="https://{}.herokuapp.com".format(APP_NAME, TOKEN))
    return "Hello from Heroku!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
