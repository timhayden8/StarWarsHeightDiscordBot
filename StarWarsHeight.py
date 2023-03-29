import requests
import json
import discord
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
            r = requests.get("https://swapi.dev/api/people")
            r=r.content
            r=json.loads(r)
            r=r['results']
            for i in r:
                if i['name'].lower() == input.lower():
                    height = i['height']
            await message.channel.send(f'{input} is {height} cm tall.')
        except:
            await message.channel.send("Sorry, this character isn't in the SWAPI Database.")
client.run('MTA5MDQxMjM1MjA3NzMwMzgxOA.GAThCG.bpUtDwMRG1outA6ICiXu66oz2mzMMb7AxAZY-g')