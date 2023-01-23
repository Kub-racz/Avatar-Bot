import discord
from discord.ext import commands

class Roles_Remove(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.message_id == 1052918322133467146: # id wiadomości, która ma reakcje odpowiadające rolom na discordzie 
            if payload.emoji.id == 853674162836733953: #league of legends
                guild = self.bot.get_guild(payload.guild_id)
                member = guild.get_member(payload.user_id)
                rola_lol = discord.utils.get(member.guild.roles, id=690562132596621332)
                await member.remove_roles(rola_lol)
            if payload.emoji.id == 756852575952699442: #among us
                guild = self.bot.get_guild(payload.guild_id)
                member = guild.get_member(payload.user_id)
                rola_amongus = discord.utils.get(member.guild.roles, id=758699987076120617)
                await member.remove_roles(rola_amongus)
            if payload.emoji.id == 899655886727942205: #Gartic phone
                guild = self.bot.get_guild(payload.guild_id)
                member = guild.get_member(payload.user_id)
                rola_gartic = discord.utils.get(member.guild.roles, id=849544530252005376)
                await member.remove_roles(rola_gartic)
            if payload.emoji.id == 899658409324974121: #aion
                guild = self.bot.get_guild(payload.guild_id)
                member = guild.get_member(payload.user_id)
                rola_aion = discord.utils.get(member.guild.roles, id=690561968368648262)
                await member.remove_roles(rola_aion)
            if payload.emoji.id == 901765915127975966: #fall guys
                guild = self.bot.get_guild(payload.guild_id)
                member = guild.get_member(payload.user_id)
                rola_fall_guys = discord.utils.get(member.guild.roles, id=901764558694264832)
                await member.remove_roles(rola_fall_guys)
            if payload.emoji.id == 901765914993758251: #minecraft
                guild = self.bot.get_guild(payload.guild_id)
                member = guild.get_member(payload.user_id)
                rola_minecraft = discord.utils.get(member.guild.roles, id=901764555410137088)
                await member.remove_roles(rola_minecraft)
            if payload.emoji.id == 901765915849408512: #don't starve 
                guild = self.bot.get_guild(payload.guild_id)
                member = guild.get_member(payload.user_id)
                rola_dst = discord.utils.get(member.guild.roles, id=901764549026410526)
                await member.remove_roles(rola_dst)
            if payload.emoji.id == 973304207123820584: #lost ark
                guild = self.bot.get_guild(payload.guild_id)
                member = guild.get_member(payload.user_id)
                rola_lost_ark = discord.utils.get(member.guild.roles, id=899276426673545227)
                await member.remove_roles(rola_lost_ark)
            if payload.emoji.id == 975807697658208266: #the forest
                guild = self.bot.get_guild(payload.guild_id)
                member = guild.get_member(payload.user_id)
                rola_forest = discord.utils.get(member.guild.roles, id=975812666926981130)
                await member.remove_roles(rola_forest)

def setup(bot):
    bot.add_cog(Roles_Remove(bot))