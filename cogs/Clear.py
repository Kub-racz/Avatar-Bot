import discord
from discord import app_commands
from discord.ext import commands
class Clear(commands.Cog):
    def __init__(self, bot: commands.Bot) ->None:
        self.bot = bot

    @commands.has_permissions(manage_messages=True)
    @app_commands.command(name = "clear", description= "Usuń x wiadomości.")
    async def clear(self, interaction: discord.Interaction, amount: int):
        await interaction.response.send_message("Wiadomości zostały usunięte.")
        await interaction.channel.purge(limit=amount+1)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Clear(bot), guilds=[discord.Object(id=663377815181459477)])