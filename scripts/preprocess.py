import re

def normalize_amharic(text):
    text = re.sub(r'[^\w\s፣።፤፥]', '', text)  # Remove strange symbols
    return text.strip()

def tokenize_amharic(text):
    return text.split()
