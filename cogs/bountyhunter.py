import discord
import json
import os
from discord.ext import commands 

class _bountyhunter(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    @commands.command() 
    async def bountyhunter(self, ctx):
        role = discord.utils.get(ctx.message.guild.roles, name='Bounty Hunter')
        if not role in ctx.author.roles:
            await ctx.author.send("You are not a bounty hunter")
            return
        embed = discord.Embed(
        title="Bounty Hunter",
        description='Dear bounty hunter',
        color= discord.Colour.green()
        )
        msg = await ctx.author.send(embed=embed)



def setup(bot):
    bot.add_cog(_bountyhunter(bot))
    print("loading bounty hunter completed")