import discord
from discord.ext import commands
import sqlite3

class Table_Level(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        db = sqlite3.connect("level.db")
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS level_toss_a_coin(guild_id INT, user_id INT, xp INT, level INT)")
        cursor.close()
        db.close()

def setup(bot):
    bot.add_cog(Table_Level(bot))