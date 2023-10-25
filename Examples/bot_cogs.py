from typing import Dict
from discord.ext import commands, ipc
from discord.ext.ipc.server import Server
from discord.ext.ipc.objects import ClientPayload

class Routes(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.ipc = ipc.Server(self.bot, secret_key="🐼")

    @commands.Cog.listener()    
    async def on_ready(self):
        await self.ipc.start()

    @Server.route()
    async def get_user_data(self, data: ClientPayload):
        user = self.get_user(int(data.user_id))
        return user._to_minimal_user_json()

async def setup(bot):
    await bot.add_cog(Routes(bot))