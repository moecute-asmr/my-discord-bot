import discord
import os
print(f"環境変数 DISCORD_TOKEN: '{os.getenv('DISCORD_TOKEN')}'")

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

token = os.getenv("MTM4MzkzNjc2OTExMTYyMTcwMw.Glrd6N.itI-uh_YHDH2sB3GzNXzWEM0dybLHtAk_tR3ps")
print(f"DISCORD_TOKEN={token}")  # ここでトークンがNoneか確認
if token is None:
    print("ERROR: DISCORD_TOKENが設定されていません！")
client.run(token)
