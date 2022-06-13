import discord
import random
from discord.ext import commands


class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name="8ball",
                      brief="Use The 8Ball",
                      description="Use The 8ball. It will decide for you.")
    async def _8ball(self, ctx, *args):
        if len(args) == 0:
            await ctx.send("Say Something")
            return
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."
            ]
        await ctx.send(f'{random.choice(responses)}')

    @commands.command(brief="Chooses one of the choices",
                      description="Chooses one of the choices")
    async def choose(self, ctx, *args):
        if len(args) < 2:
            await ctx.send("Give At Least Two Choices")
            return
        await ctx.send(f"{random.choice(args)}")

    @commands.command(brief="Make Little Goose Say Something",
                      description="Make Little Goose Say Something")
    async def say(self, ctx, *, args):
        await ctx.send(f"{args}")


def setup(client):
    client.add_cog(Fun(client))
