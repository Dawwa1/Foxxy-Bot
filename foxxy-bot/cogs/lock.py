import nextcord
from nextcord import guild
from nextcord import permissions
from nextcord.ext import commands
from nextcord.utils import get
from cogs.utils.invalidperms import invalidpermissions

class lock(commands.Cog):

    def __init__(self,bot: commands.Bot):
        self.bot=bot

    @commands.command()
    async def lock(self, ctx:commands.Context, role:int):
        overwrite = nextcord.PermissionOverwrite()
        overwrite.send_messages = False
        overwrite.read_messages = True
        g = ctx.guild
        r = g.get_role(role)
        await ctx.message.channel.set_permissions(r, overwrite=overwrite)
        embed=nextcord.Embed(title="Locked", description="This channel has now been locked by " + str(ctx.author) + " for " + str(r), color=0xff0000)
        await ctx.send(embed=embed)

    @commands.command()
    async def unlock(self, ctx:commands.Context, role:int):
        overwrite = nextcord.PermissionOverwrite()
        overwrite.send_messages = True
        overwrite.read_messages = True
        g = ctx.guild
        r = g.get_role(role)
        await ctx.message.channel.set_permissions(r, overwrite=overwrite)
        embed=nextcord.Embed(title="Unlocked", description="This channel has now been unlocked by " + str(ctx.author) + " for " + str(r), color=0xff0000)
        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(lock(bot))