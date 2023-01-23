import discord
from discord.ext import commands

class Welcome(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener() 
    async def on_member_join(self, member):
        canal = discord.utils.get(member.guild.channels, id=663377815793565719) #do wysyłania na konkretny kanał 
        canal_role = discord.utils.get(member.guild.channels, id=756046078968594493) #zmienna do kanału "role"
        rola = discord.utils.get(member.guild.roles, id=688697766330892289) # zmienna do nadawania roli przy dołączeniu na serwer
        canal_regulamin = discord.utils.get(member.guild.channels, id=684469890781937712) #zmienna do kanału regulamin
        await canal.send(f"Witaj {member.mention}.\nNadałem ci rolę Guest, więcej możesz sobie wybrać na kanale {canal_role.mention}. \nZapoznaj się też z kanałem {canal_regulamin.mention}.\n")
        await member.add_roles(rola)

def setup(bot):
    bot.add_cog(Welcome(bot))