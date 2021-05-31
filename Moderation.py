#HOW TO MAKE A BASIC MODERATION SYSTEM FOR YOUR DISCORD SERVER

#FIRST IMPORT THE REQUIRED MODULES: 

import discord 
from discord.ext import commands
from discord.ext.commands import Bot 
import os 

@bot.command()
@commands.has_permissions(kick_members=True)#ONLY PEOPLE WITH KICK PERMISSIONS CAN KICK
async def kick(ctx, user: discord.Member, *, reason=None): #KICK SOMEONE FROM YOUR DISCORD SERVER
  await user.kick(reason=reason) # PROVIDE A REASON TO KICK
  await ctx.send(f"{user} has been kicked sucessfully")

@bot.command()
@commands.has_permissions(ban_members=True) #ONLY POEPLE WITH BAN PERMISSIONS CAN BAN
async def ban(ctx, user: discord.Member, *, reason=None): #Ban someone from your server
  await user.ban(reason=reason)# PROVIDE A REASON TO BAN
  await ctx.send(f"{user} has been bannned sucessfully") #FORMAT : [!ban @user Reason]

@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
  banned_users = await ctx.guild.bans()                              #UnBan someone in your server
  member_name, member_discriminator = member.split('#')              #FORMAT : [!unban @user]

  for ban_entry in banned_users:
    user = ban_entry.user
  
  if (user.name, user.discriminator) == (member_name, member_discriminator):
    await ctx.guild.unban(user)
    await ctx.send(f"{user} has been unbanned sucessfully") #User gets unbanned
    return

with open('reports.json', encoding='utf-8') as f: 
  try:
    report = json.load(f)
  except ValueError:
    report = {}
    report['users'] = []

@bot.command(pass_context = True)
@commands.hasoermissions(ban_members=True)
async def warn(ctx,user:discord.User,*reason:str): #warn a user format: !warn @user reason 
  author = ctx.author
  if not reason:
    await ctx.send("Please provide a reason") #Just to make sure everyone provides a reason
    return
  reason = ' '.join(reason)
  await ctx.send(f'**{user.mention} has been warned by {author.name}.**') #shows who warned who
  await user.send(f'You have been warned in **{ctx.guild.name}** by **{author.name}**.') #sends the user who has been warned a dm to notify them about it
  for current_user in report['users']:
    if current_user['name'] == user.name:
      current_user['reasons'].append(reason)
      break
  else:
    report['users'].append({
      'name':user.name,
      'reasons': [reason,]
    })
  with open('reports.json','w+') as f:
    json.dump(report,f)

  with open('reports.json','w+') as f:
    json.dump(report,f)
  if len(report['users']) >= 10:
    await user.kick(reason='You reached 10 warnings') #the user automatically gets kicked when he reaches 10 warns.

@bot.command(pass_context = True)
async def warnings(ctx,user:discord.User): #See how many warns a user has
  for current_user in report['users']:
    if user.name == current_user['name']:
      await ctx.send(f"**{user.name} has been reported {len(current_user['reasons'])} times : {','.join(current_user['reasons'])}**") #this will show how many warns a user has if they have none then it will say so.
      break
  else:
    await ctx.send(f"**{user.name} has never been reported**") 
