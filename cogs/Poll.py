import discord
from discord import app_commands
from discord.ext import commands

class Poll(commands.Cog):
    def __init__(self, bot: commands.Bot) ->None:
        self.bot = bot

    @app_commands.command(name = "poll", description= "Utwórz głosowanie.")
    async def poll(self, interaction: discord.Interaction, question:str, options:int, choice_a:str, choice_b:str, choice_c:str, choice_d:str):
        if options < 2:
            await interaction.response.send_message("Aby głosowanie się odbyło musisz podać przynajmniej dwie opcje wyboru.")
            return
        if options == 2:
            embed = discord.Embed(title=f"{question}", color=0x00affa)
            embed.add_field(name="🇦", value=(choice_a), inline=True)
            embed.add_field(name="🇧", value=(choice_b), inline=True)
            await interaction.response.defer()
            msg = await interaction.followup.send(embed=embed)
            await msg.add_reaction('🇦')
            await msg.add_reaction('🇧')
        if options == 3:
            embed = discord.Embed(title=f"{question}", color=0x00affa)
            embed.add_field(name="🇦", value=(choice_a), inline=True)
            embed.add_field(name="🇧", value=(choice_b), inline=True)
            embed.add_field(name="🇨", value=(choice_c), inline=True)
            await interaction.response.defer()
            msg = await interaction.followup.send(embed=embed)
            await msg.add_reaction('🇦')
            await msg.add_reaction('🇧')
            await msg.add_reaction('🇨')
        if options == 4:
            embed = discord.Embed(title=f"{question}", color=0x00affa)
            embed.add_field(name="🇦", value=(choice_a), inline=True)
            embed.add_field(name="🇧", value=(choice_b), inline=True)
            embed.add_field(name="🇨", value=(choice_c), inline=True)
            embed.add_field(name="🇩", value=(choice_d), inline=True)
            await interaction.response.defer()
            msg = await interaction.followup.send(embed=embed)
            await msg.add_reaction('🇦')
            await msg.add_reaction('🇧')
            await msg.add_reaction('🇨')
            await msg.add_reaction('🇩')
        if options >=5:
            await interaction.response.send_message("Więcej możliwości nie sprzyja sprawnemu głosowaniu.")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Poll(bot), guilds=[discord.Object(id=663377815181459477)])