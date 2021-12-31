from datetime import datetime
import requests

def sales_query():
  #set time parameters
  time_now = datetime.now().strftime('%s')
  ref_time = int(time_now) - 60

  #set query for The Graph quary
  query = """ 
  query RecentQuery($time: BigInt!)
  {
    erc721Listings(orderBy: timePurchased, orderDirection: desc, where: {timePurchased_gte: $time}) {
      category
      id
      timeCreated
      tokenId
    }
  }
  """

  # set variable for the query - basically the time difference
  variables = {'time': ref_time}

  base_url = 'https://api.thegraph.com/subgraphs/name/aavegotchi/aavegotchi-core-matic'

  #pull data from The Graph
  response = requests.post(base_url, json={'query': query, 'variables': variables})
  raw_data = response.json()
  data = raw_data['data']['erc721Listings']
  #print(data)
  return data