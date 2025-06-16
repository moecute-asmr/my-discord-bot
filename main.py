import discord
import os

intents = discord.Intents.default()
intents.message_content = True  # ���b�Z�[�W���e��ǂނ̂ɕK�v

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'���O�C�����܂���: {client.user}')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '�҂�I':
        await message.channel.send('�ۂ�I')

token = os.getenv("DISCORD_TOKEN")
client.run(token)
