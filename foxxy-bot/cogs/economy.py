import nextcord
from nextcord import guild
from nextcord import permissions
from nextcord.ext import commands
from nextcord.utils import get
import asyncio
import json
import os
import random

os.chdir(r"C:\Users\Vova\Desktop\projects\foxxy-bot")

class economy(commands.Cog):

    def __init__(self,bot: commands.Bot):
        self.bot=bot

    @commands.command()
    async def balance(self, ctx:commands.Context):
        await open_account(ctx, user=ctx.author)

        user = ctx.author

        users = await get_bank_data()

        wallet_amt = users[str(user.id)]["wallet"]
        bank_amt = users[str(user.id)]["bank"]

        em = nextcord.Embed(title=f"{ctx.author.name}'s balance",color=0x0087FF)
        em.add_field(name="Wallet", value= wallet_amt)
        em.add_field(name="Bank", value= bank_amt)
        await ctx.send(embed = em)
        
    @commands.command()
    async def beg(self, ctx:commands.Context):
        await open_account(ctx, user=ctx.author)
        
        user = ctx.author

        users = await get_bank_data()

        earnings = random.randrange(1, 100)

        em = nextcord.Embed(title=f"Begging", description=f"Someone gave you {earnings} coins!", color=0x0087FF)
        await ctx.send(embed = em)
        
        users[str(user.id)]["wallet"] += earnings
        with open("mainbank.json", "w") as f:
            json.dump(users,f)

    @commands.command()
    async def transfer(self, ctx:commands.Context):


async def open_account(ctx:commands.Context, user):

    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0
    with open("mainbank.json", "w") as f:
        json.dump(users,f)
    return True, user

async def get_bank_data():
    with open("mainbank.json", "r") as f:
        users = json.load(f)

        return users


def setup(bot: commands.Bot):
    bot.add_cog(economy(bot))