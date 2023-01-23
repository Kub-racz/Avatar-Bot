import discord
from discord.ext import commands
import sqlite3

async def levelup(xp, level):
    if((level + 1)*100 < xp):
        return True
    else:
        return False

class Add_exp(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def addxp(self, ctx, member: discord.Member, value: int):
        db = sqlite3.connect("level.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM level_toss_a_coin WHERE guild_id = {member.guild.id} AND user_id = {member.id}")
        wynik = cursor.fetchone()
        if wynik == None:
            cursor.execute("INSERT INTO level_toss_a_coin(guild_id, user_id, xp, level) VALUES(?, ?, ?, ?)", (member.guild.id, member.id, value, 1))
        else:
            channel = self.bot.get_channel(899665814951694336) #zmienna do wysyłania wiadomości na konkretnym kanale
            if await levelup(wynik[2], wynik[3]):
                level = wynik[3] + 1
                cursor.execute("UPDATE level_toss_a_coin SET level = ? WHERE guild_id = ? AND user_id = ?", (level, member.guild.id, member.id))
                db.commit()
                await channel.send(f"Boost exp! \n {member.mention} masz {level} level. \n")
            cursor.execute("UPDATE level_toss_a_coin SET xp = ? WHERE guild_id = ? AND user_id = ?", (wynik[2]+ value, member.guild.id, member.id))
            db.commit()
            cursor.close()
            db.close()
        await channel.send(f"{member.mention} dodałem ci {value} xp.")

def setup(bot):
    bot.add_cog(Add_exp(bot))