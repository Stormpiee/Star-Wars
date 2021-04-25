import discord
import os
import sys
import json
import datetime
from discord.ext import commands 
from dotenv import load_dotenv
from open_acc import get_user_data, open_account, open_inventory
bot = commands.Bot(command_prefix = '!', case_insensitive=True)

if __name__ == "__main__":
    #get every file in ./cogs dir
    for filename in os.listdir("./cogs"):
        #check if the filename ends with .py
        if filename.endswith(".py"):
            try:
                #load <filename>
                bot.load_extension(f"cogs.{filename[:-3]}")
            except Exception as e:
                print(f"failed to load extension {filename}", file=sys.stderr)
load_dotenv()
TOKEN = os.getenv('TOKEN')
@bot.event
async def on_ready():
    print("..................")
    print("Logged on")
    print(bot.user.name)
    print(bot.user.id)
    print("..................")

@bot.event
async def on_raw_reaction_add(payload):

    messageID = 832721634409316383
    if payload.message_id != messageID:
        return

    guild = await bot.fetch_guild(payload.guild_id)
    member = await guild.fetch_member(payload.user_id)

    role1 = discord.utils.get(guild.roles, name='Citizen')
    role2 = discord.utils.get(guild.roles, name='Jedi')
    role3 = discord.utils.get(guild.roles, name='Sith')

    if role1 in member.roles:
        await member.send("You can only have one role at the time")
        return
    elif role2 in member.roles:
        await member.send("You can only have one role at the time")
        return
    elif role3 in member.roles:
        await member.send("You can only have one role at the time")
        return

    if payload.emoji.name == '\N{Large Blue Square}':
        role = discord.utils.get(guild.roles, name='Jedi')
        await member.add_roles(role)
    elif payload.emoji.name == '\N{Large Red Square}':
        role = discord.utils.get(guild.roles, name='Sith')
        await member.add_roles(role)
    elif payload.emoji.name == '\N{White Large Square}':
        role = discord.utils.get(guild.roles, name='Citizen')
        await member.add_roles(role)

@bot.event
async def on_raw_reaction_remove(payload):

    messageID = 832721634409316383
    if payload.message_id != messageID:
        return

    guild = await bot.fetch_guild(payload.guild_id)
    member = await guild.fetch_member(payload.user_id)

    if payload.emoji.name == '\N{Large Blue Square}':
        role = discord.utils.get(guild.roles, name='Jedi')
        await member.remove_roles(role)
    elif payload.emoji.name == '\N{Large Red Square}':
        role = discord.utils.get(guild.roles, name='Sith')
        await member.remove_roles(role)
    elif payload.emoji.name == '\N{White Large Square}':
        role = discord.utils.get(guild.roles, name='Citizen')
        await member.remove_roles(role)

@bot.event
async def on_member_join(member):
    with open('users.json', 'r') as f:
        users = json.load(f)
    
    await update_data(users, member)

    with open('users.json', 'w') as f:
        json.dump(users, f)

@bot.event
async def on_message(ctx):
    if (ctx.author.bot):
        return
    
    open_account(ctx.author)
    open_inventory(ctx.author)

    with open('users.json', 'r') as f:
        users = json.load(f)
    
    await update_data(users, ctx.author)
    await add_experience(users, ctx.author, 10)
    await level_up(ctx, users, ctx.author, ctx.channel)

    with open('users.json', 'w') as f:
        json.dump(users, f)
    await bot.process_commands(ctx)

async def update_data(users, user):
    if not str(user.id) in users:
        users[str(user.id)] = {}
        users[str(user.id)]['experience'] = 0
        users[str(user.id)]['level'] = 1

async def add_experience(users, user, exp):
    users[str(user.id)]['experience'] += exp

async def level_up(ctx, users, user, channel):
    while users[str(user.id)]['experience'] >= 100 * (users[str(user.id)]["level"]**1.5):
        users[str(user.id)]['experience'] -= 100 * (users[str(user.id)]["level"]**1.5)
        users[str(user.id)]['level'] += 1
        lvl_start = users[str(user.id)]['level']

        if lvl_start == 10:

            role2 = discord.utils.get(ctx.guild.roles, name='Jedi')
            role3 = discord.utils.get(ctx.guild.roles, name='Sith')

            if role2 in ctx.author.roles:
                role = discord.utils.get(ctx.guild.roles, name='Jedi Youngling')
                await user.add_roles(role)

            if role3 in ctx.author.roles:
                role = discord.utils.get(ctx.guild.roles, name='Sith Baby')
                await user.add_roles(role)

        if lvl_start == 20:

            role2 = discord.utils.get(ctx.guild.roles, name='Jedi')
            role3 = discord.utils.get(ctx.guild.roles, name='Sith')
            role5 = discord.utils.get(ctx.guild.roles, name='Sith Baby')
            role6 = discord.utils.get(ctx.guild.roles, name='Jedi Youngling')            
            
            if role2 in ctx.author.roles:
                await user.remove_roles(role6)

            if role3 in ctx.author.roles:
                await user.remove_roles(role5)

            if role2 in ctx.author.roles:
                role = discord.utils.get(ctx.guild.roles, name='Jedi Master')
                await user.add_roles(role)

            if role3 in ctx.author.roles:
                role = discord.utils.get(ctx.guild.roles, name='Sith Lord')
                await user.add_roles(role)

        em = discord.Embed(title = f"{user.name} has leveled up to level {lvl_start}", color = discord.Color.purple())
        await ctx.channel.send(embed = em)
    with open('users.json', 'w') as f:
        json.dump(users, f)
    return

@bot.command(aliases = ["train", "training"])
@commands.cooldown(1, 60*60*6, commands.BucketType.user)
async def _training(ctx):

    users = get_user_data()
    user = ctx.author    
    lvl_start = users[str(user.id)]['level']


    role2 = discord.utils.get(ctx.guild.roles, name='Jedi')
    role3 = discord.utils.get(ctx.guild.roles, name='Sith')

    if role2 in ctx.author.roles or role3 in ctx.author.roles:

        em = discord.Embed(title = f"{user}'s training has been completed", description = f"You have trained well and earned **500 exp**", color = discord.Color.purple())
        await ctx.channel.send(embed = em)

        with open('users.json', 'r') as f:
            users = json.load(f)
            
        await add_experience(users, ctx.author, 500)
        await update_data(users, ctx.author)
        await level_up(ctx, users, ctx.author, ctx.channel)

        with open('users.json', 'w') as f:
            json.dump(users, f)
    else:
        await ctx.send("You can only train as a Jedi or a Sith")

@bot.command(aliases = ["lvl", "level"])
async def _level_embed(ctx):

    users = get_user_data()
    user = ctx.author
    lvl_start = users[str(user.id)]['level']

    em = discord.Embed(title = ctx.author.name, description = f"level {lvl_start}", color = ctx.author.color)
    await ctx.channel.send(embed = em)




@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '**Cooldown**, you have to wait {:.2f}s before you can use this command again'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error

bot.run(TOKEN)