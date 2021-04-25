import discord
import json
import os
import random
import sys 
sys.path.append("./")
from open_acc import open_inventory, get_bank_data, get_user_data, get_inventory_data, open_account
from discord.ext import commands 

crafting_options = [{"id" : "001", "name" : "Blaster", "price" : 4, "item" : "Blaster part"}, 
                    {"id" : "002", "name" : "Light saber", "price" : 10, "item" : "Light saber part"}, 
                    {"id" : "003", "name" : "Republic attack cruiser", "price" : 50, "item" : "Republic attack cruiser part"},
                    {"id" : "004", "name" : "Lego 4504 Star Wars Millenium Falcon", "price" : 1000, "item" : "Lego 4504 Star Wars Millenium Falcon part"}]


shop_options = [{"id" : "001", "name" : "Blaster part", "price" : 10}, 
                    {"id" : "002", "name" : "Light saber part", "price" : 10}, 
                    {"id" : "003", "name" : "Republic attack cruiser part", "price" : 10},
                    {"id" : "004", "name" : "Lego 4504 Star Wars Millenium Falcon part", "price" : 10}]

class _crafting(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    @commands.command(aliases = ["crafting"])
    async def _craft(self, ctx):
        em = discord.Embed(title = "Crafting")

        for item in crafting_options:
            name = item["name"]
            price = item["price"]
            item = item["item"]
            em.add_field(name = name, value = f"{price} {item}", inline = False)
        await ctx.send(embed = em)


    @commands.command(aliases = ["craft"])
    async def _craft_item(self, ctx, ID = None, amount = 1):
        open_inventory(ctx.author)
        user = ctx.author
        users = get_inventory_data()

        if ID == None:
            em = discord.Embed(description = "Use `!craft <id> <amount>`",color = discord.Color.blue())
        else:

            for item in crafting_options:
                if item["id"] == ID:
                    price = item["price"]
                    name = item["name"]
                    crafting_item = item["item"]
                    break
                name = None
            
            if name == None:
                await ctx.send("Put an ID")
                return

            if amount <= 0:
                await ctx.send(f"You cannot buy less then 1 {name}")
                return
            
            total = price * amount

            user_item = users[str(user.id)][crafting_item]

            if user_item < total:
                await ctx.send(f"You need at least {total} {crafting_item}s to make {amount} {name}")
                return

            users[str(user.id)][crafting_item] -= total
            users[str(user.id)][name] += amount
            em = discord.Embed(description = f"You crafted {amount} {name} and used {total} {crafting_item}s.",color = discord.Color.blue())

        with open("inventory.json","w") as f:
            json.dump(users,f)
        await ctx.send(embed = em)


    @commands.command(aliases = ["crafting"])
    async def _craft(self, ctx):
        em = discord.Embed(title = "Crafting")

        for item in crafting_options:
            name = item["name"]
            price = item["price"]
            item = item["item"]
            em.add_field(name = name, value = f"{price} {item}", inline = False)
        await ctx.send(embed = em)


    @commands.command(aliases = ["buy"])
    async def _buy_item(self, ctx, ID = None, amount = 1):
        open_account(ctx.author)
        open_inventory(ctx.author)
        user = ctx.author
        users = get_bank_data()
        i_users = get_inventory_data()

        userbal = users[str(user.id)]["balance"]

        if ID == None:
            em = discord.Embed(description = "Use `!buy <id> <amount>`",color = discord.Color.blue())
        else:

            for item in shop_options:
                if item["id"] == ID:
                    price = item["price"]
                    name = item["name"]
                    break
                name = None
            
            if name == None:
                await ctx.send("Put an ID")
                return

            if amount <= 0:
                await ctx.send(f"You cannot buy less then 1 {name}")
                return
            
            total = price * amount

            if amount == 1:
                more = ""
            else:
                more = "'s"

            if userbal < total:
                await ctx.send(f"You need at least {total} creditss to buy {amount} {name}{more}")
                return

            users[str(user.id)]["balance"] -= total
            i_users[str(user.id)][name] += amount
            em = discord.Embed(description = f"You bought {amount} {name}{more} and payed {total} credits.",color = discord.Color.blue())

        with open("inventory.json","w") as f:
            json.dump(i_users,f)
        with open("mainbank.json","w") as f:
            json.dump(users,f)
        await ctx.send(embed = em)






def setup(bot):
    bot.add_cog(_crafting(bot))
    print("loading crafting completed")