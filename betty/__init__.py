from .bot import bot
from .web import app

VERSION = '0.0.1'

bot.add_cog(app)
bot.loop.create_task(app.run())