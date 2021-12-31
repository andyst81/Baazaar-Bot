import discord

async def sales_sort(s, channel):
  print(s)
  if s['category'] == '0':
    await channel.send('New **Unopened Portal** just sold in The Baazaar: https://aavegotchi.com/baazaar/erc721/' + s['id'])
  elif s['category'] == '2':
    await channel.send('New **Open Portal** just sold in The Baazaar: https://aavegotchi.com/baazaar/erc721/' + s['id'])
  elif s['category'] == '3':
    await channel.send('New **Gotchi** just sold in The Baazaar: https://aavegotchi.com/baazaar/erc721/' + s['id'])
  elif s['category'] == '4': 
    await channel.send('New **Realm Parcel** just sold in The Baazaar: https://aavegotchi.com/baazaar/erc721/' + s['id'])