from discord.ext import commands

class General(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(
        brief="Says Little Goose's Ping", description="Tells You Little Goose's Ping"
    )
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.client.latency * 1000)}ms")


def setup(client):
    client.add_cog(General(client))
