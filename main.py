import discord
import os
print("鍵一覧:", os.environ.keys())
print("DISCORD_TOKEN=", os.getenv("DISCORD_TOKEN"))

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
print(f"DISCORD_TOKEN={token}")  # ここでトークンがNoneか確認
if token is None:
    print("ERROR: DISCORD_TOKENが設定されていません！")
client.run(token)
