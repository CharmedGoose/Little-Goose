import discord
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
            embed.add_field(name=getattr(cog, "qualified_name", "No Category"),
                            value=("\n".join(command_signatures))
                            )
        await self.get_destination().send(embed=embed)

    async def send_cog_help(self, cog):
        embed = discord.Embed(title=cog.qualified_name,
                              colour=discord.Color.random())
        for command in cog.get_commands():
            embed.add_field(name=command.name,
                            value=command.brief)
        await self.get_destination().send(embed=embed)

    async def send_group_help(self, group):
        embed = discord.Embed(title=group.name,
                              colour=discord.Color.random())
        for index, command in enumerate(group.commands()):
            embed.add_field(name=command.name,
                            value=command.brief)
        await self.get_destination().send(embed=embed)

    async def send_command_help(self, command):
        embed = discord.Embed(title=command.name,
                              description=f"{command.description}",
                              colour=discord.Color.random())
        await self.get_destination().send(embed=embed)


intents = discord.Intents(messages=True, guilds=True,
                          reactions=True, members=True, presences=True)

client = commands.Bot(command_prefix='g!',
                      intents=discord.Intents.all(),
                      help_command=CustomHelpCommand())

starter = ["Did Anyone See The New Never Gonna Give You Up Animated Video?",
           "Did You Know Rick Astley Made Other Good Songs Like Keep Singing?",
           "Gif Or Jif?"
           ]


@tasks.loop(minutes=1)
async def spam_poop():
    channel = client.get_channel(973935616846880819)
    user = random.choice(channel.guild.members)
    await channel.send(f"*grabs <@{user.id}>*")
    await channel.send(f"*eats <@{user.id}>*")
    channel = client.get_channel(989611026603474965)
    user = random.choice(channel.guild.members)
    await channel.send(f"*grabs <@{user.id}>*")
    await channel.send(f"*eats <@{user.id}>*")


@client.event
async def on_message(message):
    if ("<@465097356874874881>" in message.content):
        await message.channel.send(
            "😔")
    if ("<@851537359588818944>" in message.content
            or "<@984459311587655690>" in message.content):
        await message.channel.send("Don't hurt goose")
    if (":dead:" in message.content):
        await message.channel.send(random.choice(starter))
    await client.process_commands(message)


@client.event
async def on_ready():
    spam_poop.start()


@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"Loaded The {extension} Cog")


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    await ctx.send(f"Unloaded The {extension} Cog")


@client.command()
async def reload(ctx, extension):
    message = await ctx.send(f"Reloading The {extension} Cog")
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")
    await message.edit(content=f"Reloaded The {extension} Cog")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
        print(f"Loaded {filename}")


client.run(os.getenv("TOKEN"))
