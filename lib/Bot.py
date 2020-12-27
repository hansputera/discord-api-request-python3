#!/bin/python3
import os
from time import sleep
import DiscordLog as Log

# Discord Conf
import requests

# Token
tokenInit = ""

# ClientUser

avatarHttp = "https://cdn.discordapp.com/avatars"

class User:
  def __init__(self, data):
    self.id = data['id']
    self.username = data['username']
    self.discriminator = data['discriminator']
    self.tag = f"{self.username}#{self.discriminator}"
    self.avatar = data['avatar']
    self.isBot = False
    self.isVerified = None

    if "bot" in data:
      self.isBot = True
      self.isVerified = data['verified']
    else:
      del self.isVerified
  
  def getAvatar(self):
    if self.avatar == None:
      return "https://cdn.discordapp.com/embed/avatars/1.png"
    else:
      return f"{avatarHttp}/{self.id}/{self.avatar}"

# ---------


# GuildStructure

class Guild:
  def __init__(self, data, token):
    self.id = data['id']
    self.name = data['name']
    self.icon = data['icon']
    if self.icon == None:
      del self.icon
    
    self.description = data['description']
    self.features = data['features']
    self.banner = data['banner']
    self.splash = data['splash']
    self.emojis = data['emojis']
    self.region = data['region']
    self.afk = {
      "channelID": data['afk_channel_id'],
      "timeout": data['afk_timeout']
    }
    if data['widget_enabled'] == True:
      self.widgetChannelID = data['widget_channel_id']
    
    self.verificationLevel = None
    
    # Verification Level
    if data['verification_level'] == 0:
      self.verificationLevel = "unrestricted"
    elif data['verification_level'] == 1:
      self.verificationLevel = "must have verified email on account"
    elif data['verification_level'] == 2:
      self.verificationLevel = "must be registered on Discord for longer than 5 minutes"
    elif data['verification_level'] == 3:
      self.verificationLevel = "must be a member of the server for longer than 10 minutes"
    elif data['verification_level'] == 4:
      self.verificationLevel = "must have a verified phone number"

    self.roles = data['roles']
    self.mfaLevel = data['mfa_level']
    self.explicitContentFilter = None

    if data['explicit_content_filter'] == 0:
      self.explicitContentFilter = "DISABLED"
    elif data['explicit_content_filter'] == 1:
      self.verificationLevel = "MEMBERS_WITHOUT_ROLES"
    elif data['explicit_content_filter'] == 2:
      self.verificationLevel = "ALL_MEMBERS"

    self.prefferedLocale = data['preferred_locale']
    self.vanityUrlCode = None

    if data['vanity_url_code'] != "no":
      self.vanityUrlCode = data['vanity_url_code']
    
    self.rulesChannelID = data['rules_channel_id']
    self.publicChannelID = data['public_updates_channel_id']

    self.ownerID = data['owner_id']
    self.owner = getUser(self.ownerID, token)

  def getRegion(self):
    return self.region
  
  def getIcon(self):
    if self.icon == None:
      return None
    else:
      return f"https://cdn.discordapp.com/icons/{self.id}/{self.icon}"

baseURL="https://discord.com/api"
api_version="8"

def getUser(userID, token):
  if isinstance(userID, str) == False:
    Log.error("Invalid userID")
  else:
    headers = printHeaders(token)
    response = requests.get(f"{baseURL}/v{api_version}/users/{userID}", headers=headers)
    if response.reason == "OK":
      json = response.json()
      userStructure = User(json)
      return userStructure

def getGuild(guildID, token):
  if isinstance(guildID, str) == False:
    Log.error("guildID is not string!")
  else:
    headers = printHeaders(token)
    response = requests.get(f"{baseURL}/v{api_version}/guilds/{guildID}", headers=headers)
    if response.reason == "OK":
      json = response.json()
      guildStructure = Guild(data=json, token=token)
      return guildStructure
    else:
      return False

def getClientUser(token):
  headers = printHeaders(token)
  response = requests.get(f"{baseURL}/v{api_version}/users/@me", headers=headers)
  if response.reason == "OK":
    json = response.json()
    userStructure = User(json)
    userStructure.token = token
    return userStructure
  else:
    return False

def printHeaders(token):
  return { "Authorization": "Bot {}".format(token), "Content-Type": "application/json", "User-Agent": "DiscordBot v{}".format(api_version) }

def validToken(token):
  headers = printHeaders(token)
  response = requests.get(f"{baseURL}/v{api_version}/gateway/bot", headers=headers)
  if response.reason == "OK":
    return response.json()
  else:
    return False

def start():
  os.system("clear")
  token = input("[TOKEN] Masukan kredensial atau token: ")
  if token == "":
    print("Token tidak boleh kosong!")
    sleep(1)
    start()
  else:
    os.system("clear")
    gateway = validToken(token)
    tokenInit = f"{token}"
    if gateway == False:
      print("Invalid token!")
      sleep(1)
      print("Mengulangi!")
      sleep(2)
      start()
    else:
      print(f"\n[ RATE LIMIT STATS ]\nTotal rate limit: {gateway['session_start_limit']['total']}\nTersisa percobaan: {gateway['session_start_limit']['remaining']}")
      user = getClientUser(token)
      print(f"\n\n[ Client User ]\nUsername: {user.username}\nDiscriminator: {user.discriminator}\nTag: {user.tag}\nBot: {user.isBot}\nVerified: {user.isVerified}\nAvatar CDN: {user.getAvatar()}")
      guildTest = getGuild("769938499116990504", token)
      if guildTest == False:
        Log.error("Guild tidak dapat ditemukan!")
      print(f"\n[ STAT GUILD {guildTest.name} ]\nGuild ID: {guildTest.id}\nGuild Name: {guildTest.name}\nGuild Desc: {guildTest.description}\nExplicit Content Filter: {guildTest.explicitContentFilter}\nVerification Level: {guildTest.verificationLevel}\nOwner: {guildTest.ownerID} | {guildTest.owner.tag}\nIcon: {guildTest.getIcon()}")