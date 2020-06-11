from aiohttp.web import Application, AppRunner, Response, TCPSite
from asyncio import ensure_future
from discord.ext.commands import Cog
from os import environ

from .bot import bot

class WebApp(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.app = Application()

    async def handler(self, request):
        return Response(text='This might be Betty\'s website sometime, I suppose.')

    async def run(self):
        self.app.router.add_get('/', self.handler)
        runner = AppRunner(self.app)
        await runner.setup()
        self.server = TCPSite(runner, port=environ.get('PORT', 80))
        await self.bot.wait_until_ready()
        await self.server.start()

    def cog_unload(self):
        ensure_future(self.server.stop)

app = WebApp(bot)