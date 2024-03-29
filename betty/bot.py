from datetime import datetime
import discord
from discord.ext.commands import Bot
from disputils import BotEmbedPaginator
from jikanpy import AioJikan, APIException
from operator import itemgetter

from .messages import DESCRIPTION_MESSAGE, ERROR_MESSAGE
from .util import is_na

bot = Bot(
    command_prefix='%',
    case_insensitive=True,
    description=DESCRIPTION_MESSAGE,
    activity=discord.Activity(type=discord.ActivityType.watching, name='anime'),
)


@bot.event
async def on_ready():
    print('Bot connected!')


@bot.command(help='Retrieves scheduled anime for a day of the week')
async def schedule(ctx, day=datetime.utcnow().strftime('%A').lower()):
    async with AioJikan() as client:
        try:
            response = await client.schedule(day)
        except APIException:
            ctx.send(ERROR_MESSAGE)
            return

    sorted_results = sorted(response[day], key=itemgetter('members'), reverse=True)
    embeds = []

    for result in sorted_results:
        e = discord.Embed(title=result['title'], description=is_na(result['synopsis']), url=result['url'])
        e.set_thumbnail(url=result['image_url'])
        e.set_footer(text=f"""{result['type']} | Score: {is_na(result['score'], float)} | \
{result['members']} members | Episodes: {is_na(result['episodes'], int)} | {result['rating']}""")
        embeds.append(e)

    paginator = BotEmbedPaginator(ctx, embeds)
    await paginator.run()


@bot.command(help='Searches for anime and manga based on a given term')
async def search(ctx, query, category='anime'):
    async with AioJikan() as client:
        try:
            response = await client.search(category, query)
        except APIException:
            await ctx.send(ERROR_MESSAGE)
            return

    sorted_results = sorted(response['results'], key=itemgetter('members'), reverse=True)
    embeds = []

    for result in sorted_results:
        e = discord.Embed(
            title=result['title'],
            description=is_na(result['synopsis']),
            url=result['url'],
            timestamp=datetime.fromisoformat(result['start_date'])
        )
        e.set_thumbnail(url=result['image_url'])

        footer = f"{result['type']} | Score: {is_na(result['score'], float)} | {result['members']} members"

        if category == 'anime':
            footer += f" | Episodes: {is_na(result['episodes'], int)} | {result['rated']}"

        e.set_footer(text=footer)

        embeds.append(e)

    paginator = BotEmbedPaginator(ctx, embeds)
    await paginator.run()


@bot.command(help='Retrieve a list of top anime and manga')
async def top(ctx, mtype='anime', subtype=None):
    async with AioJikan() as client:
        try:
            response = await client.top(mtype, subtype)
        except APIException:
            ctx.send(ERROR_MESSAGE)
            return

    embeds = []

    for result in response['top']:
        e = discord.Embed(
            title=result['title'],
            description=f"Rank: #{result['rank']}\nScore: {is_na(result['score'], float)}\nMembers: {result['members']}",
            url=result['url']
        )
        e.set_image(url=result['image_url'])

        footer = result['type']

        if mtype == 'anime':
            e.timestamp = datetime.fromisoformat(result['start_date'])
            footer += f" | Episodes: {is_na(result['episodes'], int)}"

        e.set_footer(text=footer)

        embeds.append(e)

    paginator = BotEmbedPaginator(ctx, embeds)
    await paginator.run()
