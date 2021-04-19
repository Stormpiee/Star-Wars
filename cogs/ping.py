import discord
import os
from discord.ext import commands 


class _ping(commands.Cog):

    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'pong!')

def setup(bot):
    bot.add_cog(_ping(bot))
    #print("loading ping completed")