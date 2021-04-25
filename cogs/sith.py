import discord
import json
import os
from discord.ext import commands 

class _sith(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    @commands.command(aliases = ["order66", "order_66"])
    async def _order_66(self, ctx):
        role = discord.utils.get(ctx.message.guild.roles, name='Darth Sidious')

        if not role in ctx.author.roles:
            await ctx.author.send("You are not Darth Sidious")
            return 

        embed = discord.Embed(title="Order 66", color= discord.Color.red())
        msg = await ctx.send(embed=embed)







def setup(bot):
    bot.add_cog(_sith(bot))
    #print("loading sith completed")