import discord
from discord.ext import commands
import openai
import os

bot = commands.Bot(
    command_prefix='!',
    description='Openai Api Test',
    help_command=None,
    case_insensitive=False,
    intents=discord.Intents.all(),
)


@bot.command()
async def q(ctx, *, arg):
    openai.api_key = "Api Key"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Q: Naufal\nA: Yes so Scary\n\nQ:{arg}\nA:",
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )
    await ctx.channel.send(response.choices[0].text)


@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')


async def on_message(self, message):
    print(f'Message from {message.author}: {message.content}')

bot.run(
    'Token Discord Bot')
