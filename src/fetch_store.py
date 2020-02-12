#!home/henriquegomide/github_repos/ecig-twitter/env/bin/python

from utils import fetch_twitter_api, search_twitter_twint
from time import strftime
from datetime import datetime, timedelta
import pandas as pd

import twint
import instagram_scraper as instagram

today = datetime.now()
start_date = today + timedelta(days=-2)
start_date = start_date.strftime("%Y-%m-%d")

end_date = today + timedelta(days=-1)
end_date = end_date.strftime("%Y-%m-%d")

# If twints break down - I may use this
    #data = fetch_twitter_api(start_date=start_date, end_date=end_date)
    #data.to_csv('var/data/{0}_{1}.csv'.format(start_date, end_date))


# Run twint 
# search_twitter_twint('cigarro eletronico', start_date, end_date)



# TODO
# Scrape Instragram using instagram_scraper
