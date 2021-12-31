import discord
from discord.ext import tasks
import os
from listing_query import listing_query
from listing_sort import listing_sort
from sales_query import sales_query
from sales_sort import sales_sort
from keep_alive import keep_alive

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # counting attribute to count loops
        self.counter = 0
        
        # start the task and run in  background
        self.my_background_task.start()

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print('------')

    # task runs every 60 seconds
    @tasks.loop(seconds=60) 
    async def my_background_task(self):

        # channel ID of listing channel
        listing_channel = self.get_channel(925368402602786826) 
        # channel ID of sales channel
        sales_channel = self.get_channel(925666621320736808)
        # channel ID of testing channel that counts number of cycles completed
        test_channel = self.get_channel(925664602124087386) 
        
        self.counter += 1
 
        # call any recent Baazaar listings
        listing_data = listing_query()
        if listing_data:
          for d in listing_data:
            await listing_sort(d, listing_channel)

        # call any recent Baazaar sales
        sales_data = sales_query()
        if sales_data:
          for s in sales_data:
            await sales_sort(s, sales_channel) 
        #send message once loop completed
        await test_channel.send('Baazaar Bot has completed ' + str(self.counter) + ' cycles')

    @my_background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready() # wait until the bot logs in

keep_alive()
client = MyClient()
client.run(os.getenv('TOKEN'))