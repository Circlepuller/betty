from .bot import bot
from .web import app

__version__ = '1.0.0'

bot.version = __version__
bot.add_cog(app)
bot.loop.create_task(app.run())
