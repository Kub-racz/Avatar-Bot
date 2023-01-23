import discord
from discord.ext import commands
import os
import json
import asyncio

from cogs.Welcome import Welcome
from cogs.Goodbye import Goodbye
from cogs.Kick import Kick
from cogs.Ban import Ban
from cogs.BotStatus import BotStatus
from cogs.Profanity import Profanity
from cogs.Roles import Roles
from cogs.RolesPick import Roles_Pick
from cogs.RolesRemove import Roles_Remove
from cogs.Table import Table_Level
from cogs.SpamCount import Level_Count
from cogs.SpamXP import Add_exp

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all(), application_id = 1046738531986444298)
        intents = discord.Intents.all() 
        intents.members = True
        intents.messages = True
        intents.reactions = True
    async def setup_hook(self):
        await self.load_extension(f"cogs.Gathering")
        await self.load_extension(f"cogs.Clear")
        await self.load_extension(f"cogs.Poll")
        await bot.tree.sync(guild = discord.Object(id=663377815181459477))

    async def on_ready(self):
        print("Avatar połączony z discordem.")
        await self.change_presence(activity=discord.Game(name="Seed"))

bot = MyBot()

for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")

with open('config.json') as f:
    data = json.load(f)
    token = data["TOKEN"]

async def main():
    await bot.add_cog(Welcome(bot))
    await bot.add_cog(Goodbye(bot))
    await bot.add_cog(Kick(bot))
    await bot.add_cog(Ban(bot))
    await bot.add_cog(BotStatus(bot))
    await bot.add_cog(Profanity(bot))
    await bot.add_cog(Roles(bot))
    await bot.add_cog(Roles_Pick(bot))
    await bot.add_cog(Roles_Remove(bot))
    await bot.add_cog(Table_Level(bot))
    await bot.add_cog(Level_Count(bot))
    await bot.add_cog(Add_exp(bot))

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())   
bot.run(token)