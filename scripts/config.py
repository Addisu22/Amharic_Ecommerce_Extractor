import os
from datetime import datetime, timedelta

api_id  = 24892085
api_hash = "82799197da708d168e0727508f474180"
session_name = "amharic_session"

# Remove old session file if it exists
session_file = session_name + '.session'
if os.path.exists(session_file):
    os.remove(session_file)
    print(f"Deleted old session file {session_file}")

channels = ['EthioMart', 'forfreemarket', 'helloomarketethiopia', 'classybrands', 'kuruwear' ]

# 5. Set cutoff date (last 5 days)
cutoff_date = datetime.now() - timedelta(days=4)

# 6. Prepare output folder
os.makedirs("Data", exist_ok=True)