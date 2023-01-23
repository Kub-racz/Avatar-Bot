import discord
from discord.ext import commands
import sqlite3
import random

async def levelup(xp, level):
    if(((level + 1)*100)/4 < xp):
        return True
    else:
        return False

class Level_Count(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        db = sqlite3.connect("level.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM level_toss_a_coin WHERE guild_id = {message.author.guild.id} AND user_id = {message.author.id}")
        wynik = cursor.fetchone()
        addxp = random.randrange(1,3) #bot randomowo nalicza wartość od 1 do 10 na każdą wiadomość użytkowników
        if message.author.id != 1046738531986444298: # warunek, żeby bot nie naliczał samemu sobie punktów i leveli
            if wynik == None:
                cursor.execute("INSERT INTO level_toss_a_coin(guild_id, user_id, xp, level) VALUES(?, ?, ?, ?)", (message.author.guild.id, message.author.id, addxp, 1))
            else:
                if await levelup(wynik[2], wynik[3]):
                    channel = self.bot.get_channel(899665814951694336) #zmienna do wysyłania wiadomości na konkretny kanał
                    level = wynik[3] + 1 
                    await channel.send(f"{message.author.mention} wbiłeś {level} level.")
                    cursor.execute("UPDATE level_toss_a_coin SET level = ? WHERE guild_id = ? AND user_id = ?", (level, message.author.guild.id, message.author.id))
                else:
                    level = wynik[3]
                cursor.execute("UPDATE level_toss_a_coin SET xp = ? WHERE guild_id = ? AND user_id = ?", (wynik[2] + addxp, message.author.guild.id, message.author.id))
        cursor.close()
        db.commit()
        db.close()

def setup(bot):
    bot.add_cog(Level_Count(bot))