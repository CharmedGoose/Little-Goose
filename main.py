import asyncio
import discord
from datetime import datetime, timedelta
import os
from discord.ext import commands, tasks
from dotenv import load_dotenv
import random

load_dotenv()

snipe_message_content = None
snipe_message_author = None
snipe_message_id = None


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
async def on_ready(self):
    wake_up_call.start()
    await self.client.change_presence(
        status=discord.Status.do_not_disturb, activity=discord.Game("What I Want To")
    )
    print("Little Goose Successfully Logged In!")


@commands.Cog.listener()
async def on_message_delete(self, message):

    global snipe_message_content
    global snipe_message_author
    global snipe_message_id

    snipe_message_content = message.content
    snipe_message_author = message.author
    snipe_message_id = message.id


@commands.command(
    brief="Snipes The Last Deleted Message",
    description="Snipes The Last Deleted Message",
)
async def snipe(self, message):
    if snipe_message_content is None:
        await message.channel.send("Theres nothing to snipe.")
    else:
        embed = discord.Embed(description=f"{snipe_message_content}")
        embed.set_footer(
            text=f"Asked by {message.author.name}", icon_url=message.author.avatar_url
        )
        embed.set_author(name=f"{snipe_message_author.display_name}")
        await message.channel.send(embed=embed)
        return


@client.command()
async def load(ctx, extension):
    if ctx.author.id == 851537359588818944:
        await client.load_extension(f"cogs.{extension}")
        await ctx.send(f"Loaded The {extension} Cog")


@client.command()
async def unload(ctx, extension):
    if ctx.author.id == 851537359588818944:
        await client.unload_extension(f"cogs.{extension}")
        await ctx.send(f"Unloaded The {extension} Cog")


@client.command()
async def reload(ctx, extension):
    if ctx.author.id == 851537359588818944:
        message = await ctx.send(f"Reloading The {extension} Cog")
        await client.unload_extension(f"cogs.{extension}")
        await client.load_extension(f"cogs.{extension}")
        await message.edit(content=f"Reloaded The {extension} Cog")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
        print(f"Loaded {filename}")

client.run(os.getenv("TOKEN"))
