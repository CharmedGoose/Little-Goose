import asyncio
import discord
from datetime import datetime, timedelta
import os
from discord.ext import commands, tasks
from dotenv import load_dotenv
import random

load_dotenv()


class CustomHelpCommand(commands.HelpCommand):
    def __init__(self):
        super().__init__()

    async def send_bot_help(self, mapping):
        embed = discord.Embed(title="Help", colour=discord.Color.random())
        for cog, command in mapping.items():
            filtered = await self.filter_commands(command, sort=True)
            command_signatures = [self.get_command_signature(c) for c in filtered]
            embed.add_field(
                name=getattr(cog, "qualified_name", "No Category"),
                value=("\n".join(command_signatures)),
            )
        await self.get_destination().send(embed=embed)

    async def send_cog_help(self, cog):
        embed = discord.Embed(title=cog.qualified_name, colour=discord.Color.random())
        for command in cog.get_commands():
            embed.add_field(name=command.name, value=command.brief)
        await self.get_destination().send(embed=embed)

    async def send_group_help(self, group):
        embed = discord.Embed(title=group.name, colour=discord.Color.random())
        for index, command in enumerate(group.commands()):
            embed.add_field(name=command.name, value=command.brief)
        await self.get_destination().send(embed=embed)

    async def send_command_help(self, command):
        embed = discord.Embed(
            title=command.name,
            description=f"{command.description}",
            colour=discord.Color.random(),
        )
        await self.get_destination().send(embed=embed)


intents = discord.Intents(
    messages=True, guilds=True, reactions=True, members=True, presences=True
)

client = commands.Bot(
    command_prefix="g!", intents=discord.Intents.all(), help_command=CustomHelpCommand()
)

def seconds_until_midnight():
    now = datetime.now()
    target = (now + timedelta(days=1)).replace(
        hour=4, minute=0, second=0, microsecond=0
    )
    diff = (target - now).total_seconds()
    return diff


@tasks.loop(seconds=1)
async def wake_up_call():
    await asyncio.sleep(seconds_until_midnight())
    message_channel = client.get_channel(1069413839344513044)
    await message_channel.send("<@815945583008415794> Wakey Wakey")

@client.event
async def on_ready():
    wake_up_call.start()


@client.command()
async def load(ctx, extension):
    await client.load_extension(f"cogs.{extension}")
    await ctx.send(f"Loaded The {extension} Cog")


@client.command()
async def unload(ctx, extension):
    await client.unload_extension(f"cogs.{extension}")
    await ctx.send(f"Unloaded The {extension} Cog")


@client.command()
async def reload(ctx, extension):
    message = await ctx.send(f"Reloading The {extension} Cog")
    await client.unload_extension(f"cogs.{extension}")
    await client.load_extension(f"cogs.{extension}")
    await message.edit(content=f"Reloaded The {extension} Cog")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
        print(f"Loaded {filename}")

client.run(os.getenv("TOKEN"))
