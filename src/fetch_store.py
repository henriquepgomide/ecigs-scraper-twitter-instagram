from utils import fetch_twitter
from time import strftime
from datetime import datetime, timedelta
import pandas as pd

today = datetime.now()
start_date = today + timedelta(days=-2)
start_date = start_date.strftime("%Y-%m-%d")

end_date = today + timedelta(days=-1)
end_date = end_date.strftime("%Y-%m-%d")

data = fetch_twitter(start_date=start_date, end_date=end_date)
data.to_csv('var/data/{0}_{1}.csv'.format(start_date, end_date))

