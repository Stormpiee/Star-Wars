import discord
import json
import os
import random
import sys 
sys.path.append("./")
from open_acc import open_account, get_bank_data, get_user_data, update_bank
from discord.ext import commands 

with open("txt/name.txt", "r") as q:
    name_bounty = []
    for line in q:
        line = line.strip()
        if line:
            name_bounty.append(line)

class _bountyhunter(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    @commands.command(aliases = ["b"]) 
    async def _bounty(self, ctx):

        users = get_bank_data()
        user = ctx.author
        name_b = random.choice(name_bounty)

        role = discord.utils.get(ctx.message.guild.roles, name='Bounty Hunter')

        if not role in ctx.author.roles:
            await ctx.author.send("You are not a bounty hunter")
            return
        
        

        reward = random.randint(100, 500)
        with open("txt/bounty.txt", "w") as f:
            f.write(str(reward))
            f.close
               
        embed = discord.Embed(
        title= name_b,
        description= reward,
        color= discord.Colour.green()
        )
        msg = await ctx.author.send(embed=embed)

    @commands.command(aliases = ["accept", "a"])
    async def _accept_bounty(self, ctx):
        with open("txt/bounty.txt", "r") as q:
            for line in q:
                line = line.strip()
                if line:
                    bounty = line

        if bounty == "0":
            await ctx.send("There is no bounty to accept")
            return

        users = get_bank_data()
        user = ctx.author
        
        try:
            activebounty = users[str(user.id)]["bounty"]["active"]
            rewardbounty = users[str(user.id)]["bounty"]["reward"]
        except KeyError:
            users[str(user.id)]["bounty"] = {}
            users[str(user.id)]["bounty"]["active"] = False
            users[str(user.id)]["bounty"]["reward"] = 0

            with open("mainbank.json", "w") as f:
                json.dump(users, f)
            
            users = get_bank_data()
            activebounty = users[str(user.id)]["bounty"]["active"]
            rewardbounty = users[str(user.id)]["bounty"]["reward"]

        if activebounty == True:
            await ctx.send("You already have an active bounty")
            return

        users[str(user.id)]["bounty"]["active"] = True
        users[str(user.id)]["bounty"]["reward"] = bounty

        with open("mainbank.json", "w") as f:
                json.dump(users, f)
        await ctx.send("You accepted the bounty")

        with open("txt/bounty.txt", "w") as f:
            f.write("0")
            f.close










def setup(bot):
    bot.add_cog(_bountyhunter(bot))
    #print("loading bounty hunter completed")