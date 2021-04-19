import discord
import json
import os
from discord.ext import commands 

class _jedi(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    @commands.command() 
    async def jediinfo(self, ctx):
        role = discord.utils.get(ctx.message.guild.roles, name='Jedi')
        if not role in ctx.author.roles:
            await ctx.author.send("You are not a Jedi")
            return
        embed = discord.Embed(
        title="Jedi",
        description='Dear jedi, welcome to the Jedi Order. You will start to learn the ways of the force to become a jedi master, as a master it is your task to teach the younglings the ways of the force. Before you become a master jedi there is a long path you will have to go through, you will start as a youngling yourself(watch out for Anakin Skywalker). You will train a lot and in the end you will make your own lightsaber, good luck.',
        color= discord.Colour.blue()
        )
        msg = await ctx.author.send(embed=embed)



def setup(bot):
    bot.add_cog(_jedi(bot))
    print("loading jedi completed")