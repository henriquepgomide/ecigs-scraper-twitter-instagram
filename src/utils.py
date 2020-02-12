import twitter
from usr.credentials import token_credentials
import data.keywords as kw
import pandas as pd
from string import Template
import logging

logging.basicConfig(filename='var/example.log',level=logging.INFO)

def fetch_twitter(start_date, end_date):

    # Query Builder
    q = Template('q=cigarro%20eletronico%20lang%3Apt%20until%3A$end_date%20since%3A$start_date&count=100')
    search_query = q.substitute(start_date=start_date, end_date=end_date)

    api = twitter.Api(
            consumer_key=token_credentials.CONSUMER_KEY,
            consumer_secret=token_credentials.CONSUMER_SECRET,
            access_token_key=token_credentials.ACCESS_TOKEN_KEY,
            access_token_secret=token_credentials.ACCESS_TOKEN_SECRET)

    try:
        # Query Twitter API
        query = api.GetSearch(raw_query=search_query,
                return_json=True)
        print(query['statuses'])
        
        query = query['statuses']
        data = pd.DataFrame.from_dict(pd.json_normalize(query), orient='Columns')
        data = data[['created_at', 'id_str', 'text', 
            'geo', 'coordinates', 'is_quote_status',
            'favorite_count', 'favorited', 'retweeted',
            'user.verified', 'user.friends_count', 'user.name',
            'user.screen_name', 'user.id_str', 'user.followers_count',
            'user.friends_count', 'user.created_at']]
        
        # Convert to pandas datetime
        data['created_at'] = pd.to_datetime(data['created_at'])
        data['user.created_at'] = pd.to_datetime(data['user.created_at'])
        logging.info('Data was stored from {0} to {1}'.format(start_date, end_date))
        return data

    except ValueError as e:
        logging.warning('Something was wrong when saving data from {0} to {1}'.format(start_date, end_date))
