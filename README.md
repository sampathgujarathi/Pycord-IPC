# Pycord IPC

<a href="https://pypi.org/project/pycord-ipc/" target="_blank"><img src="https://img.shields.io/pypi/v/pycord-ipc"></a>
<img src="https://img.shields.io/pypi/pyversions/pycord-ipc">

## High-performance inter-process communication library designed to work with the latest version of [Pycord](https://github.com/Pycord-Development/pycord)

This library is *based* on [Better-IPC](https://github.com/MiroslavRosenov/better-ipc).

# Installation
> ### Stable version
#### For Linux
```shell
python3 -m pip install -U pycord-ipc
```
#### For Windows
```shell
py -m pip install -U pycord-ipc
```

# Examples

### Client example
```python
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
```


### Cog example
```python
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
```


### Inside your web application
```python
from quart import Quart
from discord.ext.ipc import Client

app = Quart(__name__)
ipc = Client(secret_key="🐼")

@app.route('/user/<user>')
async def main(user):
    resp = await ipc.request("get_user_data", user_id=user)
    return str(resp.response)

if __name__ == '__main__':
    app.run()
```