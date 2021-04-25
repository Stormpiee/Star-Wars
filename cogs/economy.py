import discord
import os
import json
import random
import sys 
sys.path.append("./")
from open_acc import open_account, get_bank_data, get_user_data, update_bank
from discord.ext import commands 


class _economy(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    @commands.command(aliases = ["bal", "balance"])
    async def _balance(self, ctx):
        open_account(ctx.author)
        user = ctx.author
        users = get_bank_data()

        bal_amt = users[str(user.id)]["balance"]

        em = discord.Embed(title = f"{ctx.author.name}'s balance", color = discord.Color.dark_gold())
        em.add_field(name = "Credits", value = bal_amt)
        await ctx.send(embed = em)

    @commands.command(aliases = ["steal_wallet", "stealwallet", "stealw"])
    @commands.cooldown(1, 10800, commands.BucketType.user)
    async def _steal_wallet(self, ctx):
        role = discord.utils.get(ctx.message.guild.roles, name='Citizen')
        if not role in ctx.author.roles:
            await ctx.send("Only citizens can steal")
            return
        open_account(ctx.author)
        user = ctx.author
        users = get_bank_data()
        earnings = random.randrange(50)
        await ctx.send(f"You stole {earnings} credits")
        users[str(user.id)]["balance"] += earnings
        with open("mainbank.json", "w") as f:
            json.dump(users, f)

    @commands.command(aliases = ["kill_bounty", "killb", "kill_b"])
    @commands.cooldown(1, 21600, commands.BucketType.user)
    async def _kill_bounty(self, ctx):
        role = discord.utils.get(ctx.message.guild.roles, name='Bounty Hunter')
        if not role in ctx.author.roles:
            await ctx.send("Only bounty hunters can kill the bounty")
            return
        
        busted = random.randrange(100)
        if busted < 25:
            earnings = -300
            em = discord.Embed(title = f"{ctx.author.name} got caught", description = f"You got caught and **{earnings} credits** got taken away", color = discord.Color.dark_green())
            await ctx.send(embed = em)
        else:
            earnings = random.randrange(200, 400)
            em = discord.Embed(title = f"{ctx.author.name} eliminated the bounty", description = f"You brought in the bounty and got paid **{earnings} credits**", color = discord.Color.dark_green())
            await ctx.send(embed = em)
        open_account(ctx.author)
        user = ctx.author
        users = get_bank_data()
        users[str(user.id)]["balance"] += earnings
        with open("mainbank.json", "w") as f:
            json.dump(users, f)


def setup(bot):
    bot.add_cog(_economy(bot))
    #print("loading economy completed")