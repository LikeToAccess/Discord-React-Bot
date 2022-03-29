# -*- coding: utf-8 -*-
# filename          : main.py
# description       : Simple Discord reaction bot
# author            : LikeToAccess
# email             : liketoaccess@protonmail.com
# date              : 03-29-2022
# version           : v1.0
# usage             : python main.py
# notes             :
# license           : MIT
# py version        : 3.10.2
#==============================================================================
import discord
from discord.ext import commands


token = input("Token:\n> ")
bot = commands.Bot(command_prefix=
	[
		"please ",
	],
	help_command=None, case_insensitive=True)


@bot.command()
async def react(ctx):
	await ctx.message.add_reaction("\U0001F44D")


if __name__ == "__main__":
	bot.run(token)
