import discord

async def listing_sort(d, channel):
  #print(d)
  if d['category'] == '0':
    await channel.send('New **Unopened Portal** listed in The Baazaar: https://aavegotchi.com/baazaar/erc721/' + d['id'])
  elif d['category'] == '2':
    await channel.send('New **Open Portal** listed in The Baazaar: https://aavegotchi.com/baazaar/erc721/' + d['id'])
  elif d['category'] == '3':
    await channel.send('New **Gotchi** listed in The Baazaar: https://aavegotchi.com/baazaar/erc721/' + d['id'])
  elif d['category'] == '4': 
    await channel.send('New **Realm Parcel** listed in The Baazaar: https://aavegotchi.com/baazaar/erc721/' + d['id'])