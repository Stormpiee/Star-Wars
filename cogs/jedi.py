import discord
import json
import os
from discord.ext import commands 
from open_acc import open_account, get_bank_data, get_user_data, open_inventory, get_inventory_data

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

    @commands.command(aliases = ["jedi_train", "jt"])
    async def _jedi_training_ligthsaber(self, ctx):
        role = discord.utils.get(ctx.message.guild.roles, name='Jedi')
            if not role in ctx.author.roles:
                await ctx.author.send("You are not a Jedi")
                return

        open_account(ctx.author)
        open_inventory(ctx.author)

        with open('users.json', 'r') as f:
            users = json.load(f)

        await update_data(users, ctx.author)
        await add_experience(users, ctx.author, 100)
        await level_up(ctx, users, ctx.author, ctx.channel)

        with open('users.json', 'w') as f:
            json.dump(users, f)
        await bot.process_commands(ctx)

    async def update_data(users, user):
        if not str(user.id) in users:
            users[str(user.id)] = {}
            users[str(user.id)]['experience'] = 0
            users[str(user.id)]['force level'] = 1
            users[str(user.id)]['lightsaber level'] = 1



def setup(bot):
    bot.add_cog(_jedi(bot))
    print("loading jedi completed")