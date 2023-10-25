import asyncio
import websockets
import discord
from discord.ext import commands
from ipc.server import Server
from ipc.objects import ClientPayload

intents = discord.Intents.all()

bot = discord.Bot(intents=intents)
ipc = Server(bot, secret_key="🐼")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@Server.route()
async def get_user_data(self,data: ClientPayload):
    user = bot.get_user(int(data.user_id))
    return user._to_minimal_user_json()

async def main():
    await ipc.start()
    await bot.start('BOT_TOKEN')

if __name__ == "__main__":
    asyncio.run(main())
