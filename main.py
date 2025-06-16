import discord
import os

intents = discord.Intents.default()
intents.message_content = True  # メッセージ内容を読むのに必要

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'ログインしました: {client.user}')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == 'ぴん！':
        await message.channel.send('ぽん！')

token = os.getenv("DISCORD_TOKEN")
client.run(token)
