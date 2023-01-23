import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

class Kick(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()  # kickowanie
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="Bez powodu."):
        canal = discord.utils.get(member.guild.channels, id=663377815793565719)
        await canal.send(f"{member.mention} dostał kicka. {reason}")
        await member.kick(reason=reason)
        await member.send(f"Dostałeś kicka, {reason}")
        
def setup(bot):
    bot.add_cog(Kick(bot))