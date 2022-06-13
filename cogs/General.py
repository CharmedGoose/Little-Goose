import discord
import asyncio
from discord.ext import commands

snipe_message_content = None
snipe_message_author = None
snipe_message_id = None


class General(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(
            status=discord.Status.do_not_disturb,
            activity=discord.Game("What I Want To"))
        print("Little Goose Successfully Logged In!")

    @commands.Cog.listener()
    async def on_message_delete(self, message):

        global snipe_message_content
        global snipe_message_author
        global snipe_message_id

        snipe_message_content = message.content
        snipe_message_author = message.author
        snipe_message_id = message.id
        await asyncio.sleep(60)

        if message.id == snipe_message_id:
            snipe_message_author = None
            snipe_message_content = None
            snipe_message_id = None

    @commands.command(brief="Says Little Goose's Ping",
                      description="Tells You Little Goose's Ping")
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.client.latency * 1000)}ms")

    @commands.command(brief="Snipes The Last Message",
                      description="Snipes The Last Message")
    async def snipe(self, message):
        if snipe_message_content is None:
            await message.channel.send("Theres nothing to snipe.")
        else:
            embed = discord.Embed(description=f"{snipe_message_content}")
            embed.set_footer(
                text=f"Asked by {message.author.name}",
                icon_url=message.author.avatar_url)
            embed.set_author(name=f"{snipe_message_author.display_name}")
            await message.channel.send(embed=embed)
            return


def setup(client):
    client.add_cog(General(client))
