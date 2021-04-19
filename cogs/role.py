import discord
from discord.ext import commands 

class _role(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    @commands.command()
    async def Side(self, ctx):
        embed = discord.Embed(
        title="Choose a side",
        description='Choose which side you want to be on.'
        )
        msg = await ctx.send(embed=embed)
        await msg.add_reaction("🟦")
        await msg.add_reaction("🟥")
        await msg.add_reaction("⬜")

def setup(bot):
    bot.add_cog(_role(bot))
    #print("loading role completed")