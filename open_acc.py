import discord
import os
import json
import random
from discord.ext import commands 

def open_account(user):
    users = get_bank_data()

    if str(user.id) in users: 
        return
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["balance"] = 0

    with open("mainbank.json", "w") as f:
        json.dump(users, f)
    return

def get_bank_data():
    with open("mainbank.json", "r") as f:
        users = json.load(f)
    return users

def update_bank(change):
    with open("mainbank.json", "w") as f:
        json.dump(users, f)

def get_user_data():
    with open("users.json", "r") as f:
        users = json.load(f)
    return users