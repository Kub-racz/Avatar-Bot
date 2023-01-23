import discord
from discord.ext import commands

class Roles(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def Roles(self, message, ctx):
        """Komenda do nadawania roli. Role odpowiadają grom w które grywamy."""
        if message.author.id == 282471608818466819:
            channel = self.bot.get_channel(756046078968594493) #do wysyłania na konkretny kanał
            embed = discord.Embed(title="Role Serwera", color=0x00affa)
            embed.add_field(name="Lista gier w które gramy,", value="wybierz rolę gry, aby mieć podlgąd do kanałów.", inline=False)
            msg = await channel.send(embed=embed)
            await msg.add_reaction(':lol:853674162836733953') #league of legends
            await msg.add_reaction(':AmongUs_Shhhhh:756852575952699442') #among us
            await msg.add_reaction(':Gartic_Phone_logo:899655886727942205') #Gartic phone
            await msg.add_reaction(':aion:899658409324974121') #aion
            await msg.add_reaction(':fg:901765915127975966') #fall guys
            await msg.add_reaction(':mc:901765914993758251') #minecraft
            await msg.add_reaction(':dst:901765915849408512') #don't starve 
            await msg.add_reaction(':lost_ark:973304207123820584') #lost ark
            await msg.add_reaction(':theforest:975807697658208266') #the forest
        else:
            await ctx.channel.send("Tylko Kubracz może używać tej komendy.")

def setup(bot):
    bot.add_cog(Roles(bot))