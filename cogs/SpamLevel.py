import discord
from discord.ext import commands
import sqlite3

class ShowLevel(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def level(self, ctx):
        db = sqlite3.connect("level.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM level_toss_a_coin WHERE guild_id = {ctx.author.guild.id} AND user_id = {ctx.author.id}")
        wynik = cursor.fetchone()
        if wynik == None:
            channel = self.bot.get_channel(899665814951694336) #zmienna do wysyłania wiadomości na konkretny kanał
            await channel.send("Nic jeszcze nie napisałeś.")
        else:
            channel = self.bot.get_channel(899665814951694336) #zmienna do wysyłania wiadomości na konkretny kanał
            await channel.send(f"Level! Masz {wynik[2]} xp oraz {wynik[3]} level.")
        cursor.close()
        db.close()

def setup(bot):
    bot.add_cog(ShowLevel(bot))