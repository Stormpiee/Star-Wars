import discord
import os
import json
import random
import sys 
sys.path.append("./")
from open_acc import open_account, get_bank_data, get_user_data, open_inventory, get_inventory_data
from discord.ext import commands 

class _storage(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    @commands.command(aliases = ["inventory"])
    async def _inventory(self, ctx):
        open_inventory(ctx.author)
        users = get_inventory_data()
        user = ctx.author



        lsp = users[str(user.id)]["Light saber part"]
        blp = users[str(user.id)]["Blaster part"]
        bl = users[str(user.id)]["Blaster"]
        ls = users[str(user.id)]["Light saber"]
        racp = users[str(user.id)]["Republic attack cruiser part"]
        rac = users[str(user.id)]["Republic attack cruiser"]
        lego4504p = users[str(user.id)]["Lego 4504 Star Wars Millenium Falcon part"]
        lego4504 = users[str(user.id)]["Lego 4504 Star Wars Millenium Falcon"]


        em = discord.Embed(title = f"{user.name}'s inventory", description = "All your items", color = discord.Color.purple())
        if lsp > 0:
            em.add_field(name= "Light saber part", value= lsp)
        if blp > 0:
            em.add_field(name= "Blaster part", value= blp)
        if racp > 0:
            em.add_field(name= "Republic attack cruiser part", value= racp)
        if ls > 0:
            em.add_field(name= "Light saber", value= ls)
        if bl > 0:
            em.add_field(name= "Blaster", value= bl)
        if rac > 0:
            em.add_field(name= "Republic attack cruiser", value= rac)
        if lego4504p > 0:
            em.add_field(name= "Lego 4504 Star Wars Millenium Falcon part", value= lego4504p)
        if lego4504 > 0:
            em.add_field(name= "Lego 4504 Star Wars Millenium Falcon", value= lego4504)
        
        await ctx.channel.send(embed = em)


def setup(bot):
    bot.add_cog(_storage(bot))
    #print("loading storage completed")
        