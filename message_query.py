import requests

def message_query:
  query = """ 
  query RecentQuery($time: BigInt!)
  {
    erc721Listings(orderBy:timeCreated, orderDirection: desc, where: {timeCreated_gte: $time}) {
      category
      id
      timeCreated
    }
  }
  """

  base_url =    'https://api.thegraph.com/subgraphs/name/aavegotchi/aavegotchi-core-matic'

  variables = 

  #pull data from The Graph
  response = requests.post(base_url, json={'query': query, 'variables': variables})
  raw_data = response.json()
  data = raw_data['data']['erc721Listings']
  #print(data)
  return data