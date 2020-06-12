from dotenv import load_dotenv
from os import environ

from betty import bot

load_dotenv()

if __name__ == '__main__':
    bot.run(environ.get('BOT_TOKEN', ''))
