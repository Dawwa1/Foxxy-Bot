import nextcord
from nextcord import guild
from nextcord import permissions
from nextcord.ext import commands
from nextcord.utils import get
import asyncio

class poll(commands.Cog):

    def __init__(self,bot: commands.Bot):
        self.bot=bot

    @commands.command()
    async def poll(self, ctx:commands.Context, *, arg):
        embed=nextcord.Embed(title=arg, description="", color=0x0AA2E9)
        msg = await ctx.send(embed=embed)
        await msg.add_reaction("✅")
        await msg.add_reaction("🤷")
        await msg.add_reaction("❌")

def setup(bot: commands.Bot):
    bot.add_cog(poll(bot))