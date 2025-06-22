import pandas as pd
import os

path = "Data/messages.csv"
messages = []

def save_message(msg):
    global messages
    messages.append(msg)
    df = pd.DataFrame(messages)
    os.makedirs("Data", exist_ok=True)
    df.to_csv(path, index=False)
