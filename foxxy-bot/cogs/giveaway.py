import nextcord
from nextcord import guild
from nextcord import permissions
from nextcord.ext import commands
from nextcord.utils import get
import asyncio

class giveaway(commands.Cog):

    def __init__(self,bot: commands.Bot):
        self.bot=bot

    @commands.command()
    async def giveaway(self, ctx:commands.Context, *, arg):
        pass

def setup(bot: commands.Bot):
    bot.add_cog(giveaway(bot))