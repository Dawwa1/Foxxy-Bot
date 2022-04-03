from nextcord.ext import commands
import nextcord
from cogs.utils.invalidperms import invalidpermissions

class ban(commands.Cog):
    # Received ping commands

    def __init__(self,bot: commands.Bot):
        self.bot=bot

    @commands.command()
    async def ban(self, ctx:commands.Context, member: nextcord.Member = None, reason = None):
        if not ctx.message.author.guild_permissions.kick_members:
            await invalidpermissions(ctx)
        else:
            await member.ban(reason=reason)
            embed=nextcord.Embed(title="Ban Command", description="", color=0xff0000)
            embed.add_field(name="Offender", value=str(member), inline=False),
            embed.add_field(name="Reason", value=reason, inline=False),
            embed.add_field(name="Moderator", value=ctx.message.author, inline=False)
            await ctx.send(embed=embed)

    @commands.command()
    async def unban(self, ctx:commands.Context, member: nextcord.Object, reason = None):
        if not ctx.message.author.guild_permissions.kick_members:
            await invalidpermissions(ctx)
        else:
            member=int(member)
            for i in await ctx.guild.bans():
                user=i.user
                if user.id == member:
                    await ctx.guild.unban(user, reason=reason)
                    embed=nextcord.Embed(title="Unban Command", description="", color=0xff0000)
                    embed.add_field(name="Offender", value=str(member), inline=False),
                    embed.add_field(name="Reason", value=reason, inline=False),
                    embed.add_field(name="Moderator", value=ctx.message.author, inline=False)
                    await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(ban(bot))