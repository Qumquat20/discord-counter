#!/usr/bin/python3

#	Author: Qumquat
#	Date: April 2020
#	Project: Discord bot to count the amount of times a certain word is said

import discord
import time
import asyncio
from collections import OrderedDict
from discord.ext import commands
import os.path
import pickle


token = open("token.txt","r").readline()
client = commands.Bot(command_prefix = '!')


def get_int(user):
	points = pickle.load(open('points.p','rb'))
	if user in points:
		global score
		points = pickle.load(open('points.p','rb'))
		score = points[user]
		return score
	else:
		pass
            
def write_int(user):
	points = pickle.load(open('points.p','rb'))
	if user not in points:
		points.update( {user: 1} )
		pickle.dump(points,open('points.p','wb'))
	else:
		points[user] = int(points[user]) + 1
		pickle.dump(points,open('points.p','wb'))
		print(points[user])

def rw(user):
	get_int(user)
	write_int(user)

def rem_dup(word):
	return "".join(OrderedDict.fromkeys(word))

def get_ncount(user):
	get_int('{}'.format(str(user)))
	print(score)
	global msg
	msg = 'This user has said {} N-Words'.format(score)
	return msg

@client.command()
async def test(ctx):
	await ctx.send('Alive')

@client.command()
async def ncount(ctx, user : discord.User):
	uid = user.id
	get_ncount(uid)
	await ctx.send(msg)


@client.event
async def on_ready():
	print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	await client.process_commands(message)

	print(message.content)
	msgcon = message.content.casefold()
	print(msgcon)
	msgcon = msgcon.replace(" ","")
	print(msgcon)
	msgcon = rem_dup(msgcon)
	print(msgcon)

	if 'niger' in msgcon or 'ngier' in msgcon or 'niga' in msgcon or msgcon == 'nig':
		print('nigg detected')
		print(message.author, message.author.id,'\n')
		uid = message.author.id
		rw(uid)


client.run(token)
