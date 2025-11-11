__all__ = ["client", "DISCORD_TOKEN"]
from dotenv import load_dotenv
import discord
import os
from app.chatgpt_ai.openai import chatgpt_response

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')

    async def on_message(self, message):
        print(message.content)
        if message.author == self.user:
            return
        command, user_message = None, None

        for text in ['/ask', '/chat']:
            if message.content.startswith(text):
                command = message.content.split(' ')[0]
                user_message = message.content.replace(text, '')
                print(command, user_message)

        if command == '/ask' or command == '/chat':
            bot_response = chatgpt_response(prompt = user_message)
            await message.channel.send(bot_response)
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
       
    