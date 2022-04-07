import nextcord
from nextcord import guild
from nextcord import permissions
from nextcord.ext import commands
from nextcord.utils import get
import asyncio

from cogs.utils.invalidperms import invalidpermissions

class nuke(commands.Cog):

    def __init__(self,bot: commands.Bot):
        self.bot=bot

    @commands.command()
    async def nuke(self, ctx:commands.Context):
        boom = r'boom.gif'
        c = ctx.channel
        if not ctx.message.author.guild_permissions.kick_members:
            await invalidpermissions(ctx)
        else:
            await c.purge(bulk=True)
            msg = await c.send(file=nextcord.File(boom))
            await msg.delete(delay=10)

def setup(bot: commands.Bot):
    bot.add_cog(nuke(bot))