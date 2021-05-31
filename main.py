#IMPORT ALL THE MODULES YOU NEED
# THIS CODE IS SPECIALLY FOR PEOPLE WHO CODE ON REPLIT.COM
import discord 
from discord.ext import commands
from discord.ext.commands import Bot 
import os 


bot = Bot("!") #<-- Put whatever prefix you want Im using " ! "

@bot.event
async def on_ready():
await bot.change_presence(activity=discord.Game("!help"))

#lets make a test command to see if the bot is working: 

@bot.command()
async def test(ctx):
  await ctx.send("Command Executed") #<--- Now when you type !test in your discord chat it should say "Command Excecuted"
  
@bot.command() #Lets make a basic embed
async def embed(ctx):
emb = discord.Embed(title="title" , description = "description" , color = 0x800080) #To set the color of the embed get the hex of any colour you want and then put 0x and the hex
emb.set_image(url="your image url") #The url should be a direct url otherwise it wont work
emb.add_field(name="Name" , value="\
`abcd`\nabcd\nabcd\nabcd", #the \n is to make it look good and the abcd abcd is the thing you want to put
inline=False) 
emb.set_footer(text="text" , icon_url = "icon_url") #input icon url and text

my_secret = os.environ['TOKEN'] #go to Secrets(Environment variables) Then put whatever you want as the key for me I have used "token" then you can use that key to access the thing. In the "values" section you input the bots token.

bot.run(my_secret) #run the bot.
