import discord
import os
import sys 
sys.path.append("./")
from discord.ext import commands 

#with open("txt/childslayer.txt", "r") as q:
    #child_slayer = []
    #for line in q:
        #line = line.strip()
        #if line:
            #child_slayer.append(line)

class _ping(commands.Cog):

    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    @commands.command()
    async def cum(self, ctx):
        await ctx.send("Damn calm down horny fuck the boat scene isn't over yet")


    @commands.command(aliases = ["cs", "childslayer"])
    async def _child_slayer_9000(self, ctx):

        embed = discord.Embed(
        title= "Child Slayer 9000", 
        description = "Sit down take a deap breath and relax with the picture of the Child Slayer 9000 used in episode III Revenge of the sith at 1:23:30", 
        color= discord.Colour.blue())
        embed.set_image(url = "https://assets.catawiki.nl/assets/2021/1/30/b/5/8/b58ab7af-acb8-4dfb-8c25-8538d3183fb0.jpg")
        msg = await ctx.send(embed=embed)

        

def setup(bot):
    bot.add_cog(_ping(bot))
    #print("loading ping completed")