import discord
from discord.ext import commands
from discord.ext.commands import has_permissions # importowanie komendy od banowania z pozwoleniem

class Ban(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()  # banowanie
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="Na pewno jest jakiś powód."):
        #"""Komenda do banowania (tylko dla adminów)"""
        canal = discord.utils.get(member.guild.channels, id=663377815793565719) #zmienna do wysyłania na konkretny kanał
        await canal.send(f"{member.mention} został zbanowany. {reason}")
        await member.ban(reason=reason)
        await member.send(f"Dostałeś bana, {reason}")

def setup(bot):
    bot.add_cog(Ban(bot))