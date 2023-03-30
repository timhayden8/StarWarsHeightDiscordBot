import requests
import json
import discord
#Connect to discord API and start bot. Bot listens for "!starwarsheight". It then responds then waits for a response. 
#The response is captured as a variable.
intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!StarWarsHeight'):
        await message.channel.send("Who's Height do you want to know?")
        message = await client.wait_for('message')
        input = message.content
        try:
#A get request is sent to the star war's API, pulling down a list of characters. The response is then parsed for the character name taken from discord
#From this dictionary, the character's height is saved as a variable and sent to the discord API.
            r = requests.get("https://swapi.dev/api/people")
            r=r.content
            r=json.loads(r)
            r=r['results']
            for i in r:
                if i['name'].lower() == input.lower():
                    height = i['height']
            await message.channel.send(f'{input} is {height} cm tall.')
#If the height or character can't be found, the bot sends this error message.
        except:
            await message.channel.send("Sorry, this character isn't in the SWAPI Database.")
client.run("<YOUR BOT TOKEN HERE>")
