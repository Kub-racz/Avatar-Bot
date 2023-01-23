import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

class BotStatus(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()  # ustawienie statusu bota: "w grze:"
    async def botgame(self, ctx, *, Game):
        await self.bot.change_presence(activity=discord.Game(name=Game))

    @commands.command() 
    async def botstream(self, ctx, *, stream):
        await self.bot.change_presence(activity=discord.Streaming(name=stream, url="https://www.twitch.tv/directory/game/Lost%20Ark"))

    @commands.command() # ustawienie statusu bota: "słucha:"
    async def botmusic(self, ctx, *, music):
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=music))

    @commands.command() # ustawienie statusu bota: "ogląda:"
    async def botwatch(self, ctx, *, film):
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=film))

    @commands.Cog.listener() # wysyła wiadomość na kanał, gdzie użytkownik nie sprecyzował działań bota
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Nie rozumiem. Spróbuj podać dane. ")
def setup(bot):
    bot.add_cog(BotStatus(bot))