import discord
import os
import json
import random
import sys 
sys.path.append("./")
from open_acc import open_account, get_bank_data, get_user_data
from discord.ext import commands 

class _economy(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    @commands.command(aliases = ["i", "inventory"])
    async def _inventory(self, ctx):

        