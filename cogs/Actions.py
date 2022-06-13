import discord
from discord.ext import commands


class Actions(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief="Honk At Someone", description="Honk At Someone")
    async def honk(self, ctx, args):
        user = self.client.get_user(ctx.message.mentions[0].id)
        embed = discord.Embed(
            title=f"{ctx.author.display_name} Honks At {user.display_name}",
            colour=discord.Color.random()
        )
        id = "31b7344a138dac565a1c31fe4a1dce78"
        embed.set_image(
            url=f"https://i.pinimg.com/originals/31/b7/34/{id}.gif")
        await ctx.send(embed=embed)

    @commands.command(brief="Punch Someone", description="Punch Someone")
    async def punch(self, ctx):
        user = self.client.get_user(ctx.message.mentions[0].id)
        embed = discord.Embed(
            title=f"{ctx.author.display_name} Punches {user.display_name} ✊💢",
            colour=discord.Color.random()
        )
        embed.set_image(
            url="https://i.gifer.com/9eUJ.gif")
        await ctx.send(embed=embed)

    @commands.command(brief="Kick Someone", description="Kick Someone")
    async def kick(self, ctx):
        user = self.client.get_user(ctx.message.mentions[0].id)
        embed = discord.Embed(
            title=f"{ctx.author.display_name} Kicks {user.display_name} 🦵💢",
            colour=discord.Color.random()
        )
        embed.set_image(
            url="https://c.tenor.com/xJyw7SRtDRoAAAAC/anime-punch.gif")
        await ctx.send(embed=embed)

    @commands.command(brief="Kiss Someone", description="Kiss Someone")
    async def kiss(self, ctx, args):
        user = self.client.get_user(ctx.message.mentions[0].id)
        name = ctx.author.display_name
        embed = discord.Embed(
            title=f"{name} Kisses {user.display_name} 👩‍❤️‍💋‍👨",
            colour=discord.Color.random()
        )
        id = "aniyuki-anime-gif-kiss-33"
        embed.set_image(
            url=f"https://aniyuki.com/wp-content/uploads/2021/07/{id}.gif")
        await ctx.send(embed=embed)

    @commands.command(brief="Hug Someone", description="Hug Someone")
    async def hug(self, ctx, args):
        user = self.client.get_user(ctx.message.mentions[0].id)
        embed = discord.Embed(
            title=f"{ctx.author.display_name} Hugs {user.display_name} 🫂",
            colour=discord.Color.random()
        )
        embed.set_image(
            url="https://i.gifer.com/2QEa.gif")
        await ctx.send(embed=embed)

    @commands.command(brief="Poke Someone", description="Poke Someone")
    async def poke(self, ctx, args):
        user = self.client.get_user(ctx.message.mentions[0].id)
        embed = discord.Embed(
            title=f"{ctx.author.display_name} Pokes {user.display_name}",
            colour=discord.Color.random()
        )
        embed.set_image(
            url="https://c.tenor.com/3dOqO4vVlr8AAAAC/poke-anime.gif")
        await ctx.send(embed=embed)

    @commands.command(brief="Slap Someone", description="Slap Someone")
    async def slap(self, ctx, args):
        user = self.client.get_user(ctx.message.mentions[0].id)
        embed = discord.Embed(
            title=f"{ctx.author.display_name} Slaps {user.display_name} 🤚💢",
            colour=discord.Color.random()
        )
        embed.set_image(
            url="https://c.tenor.com/rVXByOZKidMAAAAd/anime-slap.gif")
        await ctx.send(embed=embed)

    @commands.command(brief="Bonk Someone", description="Bonk Someone")
    async def bonk(self, ctx, args):
        user = self.client.get_user(ctx.message.mentions[0].id)
        embed = discord.Embed(
            title=f"{ctx.author.display_name} Bonks {user.display_name}🧹💢🤕",
            colour=discord.Color.random()
        )
        embed.set_image(
            url="https://c.tenor.com/qvvKGZhH0ysAAAAC/anime-girl.gif")
        await ctx.send(embed=embed)

    @commands.command(brief="Yeet Someone", description="Yeet Someone")
    async def yeet(self, ctx, args):
        user = self.client.get_user(ctx.message.mentions[0].id)
        embed = discord.Embed(
            title=f"{ctx.author.display_name} Yeets {user.display_name}",
            colour=discord.Color.random()
        )
        embed.set_image(
            url="https://c.tenor.com/gISSJc70lH4AAAAC/yeet-naruto.gif")
        await ctx.send(embed=embed)

    @commands.command(brief="Stare At Someone", description="Stare At Someone")
    async def stare(self, ctx, args):
        user = self.client.get_user(ctx.message.mentions[0].id)
        embed = discord.Embed(
            title=f"{ctx.author.display_name} Stares At {user.display_name} 😶",
            colour=discord.Color.random()
        )
        embed.set_image(
            url="https://c.tenor.com/W_o-X6KNuCYAAAAC/anime-stare.gif")
        await ctx.send(embed=embed)

    @commands.command(brief="Cuddle Someone", description="Cuddle Someone")
    async def cuddle(self, ctx, args):
        user = self.client.get_user(ctx.message.mentions[0].id)
        embed = discord.Embed(
            title=f"{ctx.author.display_name} Cuddles {user.display_name}",
            colour=discord.Color.random()
        )
        embed.set_image(
            url="https://media.giphy.com/media/PHZ7v9tfQu0o0/giphy.gif")
        await ctx.send(embed=embed)

    @commands.command(brief="Insult Someone", description="Insult Someone")
    async def insult(self, ctx, args):
        user = self.client.get_user(ctx.message.mentions[0].id)
        embed = discord.Embed(
            title=f"{ctx.author.display_name} Insults {user.display_name}",
            colour=discord.Color.random()
        )
        embed.set_image(
            url="https://c.tenor.com/LQDCtZP0GpYAAAAC/anime-insult.gif")
        await ctx.send(embed=embed)

    @commands.command(brief="Nom On Someone", description="Nom On Someone")
    async def nom(self, ctx, args):
        user = self.client.get_user(ctx.message.mentions[0].id)
        embed = discord.Embed(
            title=f"{ctx.author.display_name} Noms On {user.display_name}",
            colour=discord.Color.random()
        )
        embed.set_image(
            url="https://i.imgur.com/Ns1RBzX.gif")
        await ctx.send(embed=embed)

    @commands.command(brief="High Five Someone", description="High Five Someone")
    async def highfive(self, ctx, args):
        user = self.client.get_user(ctx.message.mentions[0].id)
        name = ctx.author.display_name
        embed = discord.Embed(
            title=f"{name} High Fives {user.display_name}🖐️",
            colour=discord.Color.random()
        )
        embed.set_image(
            url="https://i.gifer.com/Pvwh.gif")
        await ctx.send(embed=embed)

    @commands.command(brief="Bite Someone", description="Bite Someone")
    async def bite(self, ctx, args):
        user = self.client.get_user(ctx.message.mentions[0].id)
        embed = discord.Embed(
            title=f"{ctx.author.display_name} Bited {user.display_name}",
            colour=discord.Color.random()
        )
        embed.set_image(
            url="https://c.tenor.com/w4T323o46uYAAAAC/anime-bite.gif")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Actions(client))
