import discord
import requests

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
	print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
	# print(message.author)
	if message.author == client.user:
		return
	if message.content.startswith('$echo'):
		await message.channel.send(message.content[5:])
	elif message.content.startswith('$hello') or message.content.startswith('$hi'):
		if message.author.id == 279599465277554688:
			await message.channel.send('hi ruzayne :)')
		elif message.author.id == 317884502934552596:
			await message.channel.send(':poop:')
		elif message.author.id == 318320306827689985:
			await message.channel.send('gwen: this is the closest the skrubs have to a glaggle')
		elif message.author.id == 540738469710921729:
			await message.channel.send('you are so sex see and you juble my squiggle bone :blush:')
		elif message.author.id == 319091042123251713:
			await message.channel.send('hi arthur did you know .')
		elif message.author.id == 1109854683406802944:
			await message.channel.send('hey there!!1! woud you like some glognut pancakes :-)')
		elif message.author.id == 849298091457904650:
			await message.channel.send(file=discord.File('morgie.gif'))
		else:
			await message.channel.send('joyous salutations')
	elif message.content.endswith('quoi') or message.content.endswith('quoi?'):
			await message.channel.send('feur')
client.run('MTEwOTg1NDY4MzQwNjgwMjk0NA.GmRV3h.mg99-TTbit4RGXebq0cEHm8OWt1wpkYBt4CShE')