import discord
from discord import app_commands
from discord.ext import commands
class Gathering(commands.Cog):
    def __init__(self, bot: commands.Bot) ->None:
        self.bot = bot

    @app_commands.command(name = "gathering", description= "Napisz na co zbierasz, kiedy, podaj godzinę i minutę")
    async def gathering(self, interaction: discord.Interaction, what:str, when: str, hour: int, minute:int) -> None:
        embed = discord.Embed(title=f"{what}", color=0x00affa)
        embed.add_field(name="Kiedy:", value=when, inline=False)
        embed.add_field(name="O której:", value=(f"{hour}:{minute}"), inline=False)
        embed.add_field(name="Kliknij w '✅' lub '❌'", value=("żeby inni wiedzieli czy masz czas."), inline=False)
        await interaction.response.defer()
        msg = await interaction.followup.send(embed=embed)
        await msg.add_reaction('✅')
        await msg.add_reaction('❌')

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Gathering(bot), guilds=[discord.Object(id=663377815181459477)])