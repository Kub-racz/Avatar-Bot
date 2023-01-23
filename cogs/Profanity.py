import discord
from discord.ext import commands

with open('wulgaryzmy.txt', 'r') as f:
    words = f.read()
    badwords = words.splitlines()

class Profanity(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener() #bot reaguje na wulgaryzmy 
    async def on_message(self, message):
        msg = message.content
        for word in badwords:
            if word in msg:
                await message.channel.send("Nie powinieneś używać takich słów")
                break
            
def setup(bot):
    bot.add_cog(Profanity(bot))