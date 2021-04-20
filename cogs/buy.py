import discord
import datetime
from discord.ext import commands 

class _shop(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    @commands.command(aliases = ["bm"])
    async def _blackmarket(self, ctx):
        embedVar = discord.Embed(title="Title", description="Desc", color=0x00ff00)
        embedVar.add_field(name="Field1", value="hi", inline=False)
        embedVar.add_field(name="Field2", value="hi2", inline=False)
        await ctx.send(embed=embedVar)

def setup(bot):
    bot.add_cog(_shop(bot))
    #print("loading buy completed")