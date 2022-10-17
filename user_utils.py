import discord
from discord.ext import commands
import wikipediaapi


def addEmbedField(emb, name, value):
    emb.add_field(name=name, value=value)
    return emb


class UserUtilsCog(commands.Cog):

    @commands.command()
    async def wiki(self, ctx, title: str, language='en'):

        emb = discord.Embed(title=f"{title}", color=discord.Color.random())
        emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)

        wiki_wiki = wikipediaapi.Wikipedia(
            language=language,
            extract_format=wikipediaapi.ExtractFormat.WIKI
        )

        page_py = wiki_wiki.page(title)
        summary = page_py.summary
        text = page_py.text

        emb = addEmbedField(emb, "Page - Summary:", f"{summary[0:1000]}")
        emb = addEmbedField(emb, "Page - Text:", f"{text[0:1000]}")
        print(page_py.summary)

        await ctx.send(embed=emb)
