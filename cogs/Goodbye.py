import discord
from discord.ext import commands

class Goodbye(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()  # pożegnanie po wyjściu z serwera
    async def on_member_remove(self, member):
        canal = discord.utils.get(member.guild.channels, id=663377815793565719) #zmienna do wysyłania na konkretny kanał
        await canal.send(f"{member.mention} opuścił serwer.")

def setup(bot):
    bot.add_cog(Goodbye(bot))