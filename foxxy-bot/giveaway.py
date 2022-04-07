from lib2to3.pytree import convert
import nextcord
from nextcord import guild
from nextcord import permissions
from nextcord.ext import commands
from nextcord.utils import get
import asyncio

class giveaway(commands.Cog):

    def __init__(self,bot: commands.Bot):
        self.bot=bot

    async def convert(time):
        pos = ["s","m","h","d"]

        time_dict = {"s" : 1, "m" : 60, "h" : 3600, "d": 3600*24}

        unit = time[-1]

        if unit not in pos:
            return -1
        try:
            val = int(time[:-1])
        except:
            return -2

        return val * time_dict[unit]

    @commands.command()
    async def giveaway(self, ctx:commands.Context, time, *, arg):
        d = []
        d.insert(1, time)
        print(d)
        duration = convert(d[1])
        print(duration)
        m = embed=nextcord.Embed(title=arg, description="", color=0xff0000)
        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(giveaway(bot))