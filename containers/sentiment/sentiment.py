import json
from textblob import TextBlob

with open('/app/input.json') as f:
    text = json.load(f)

analysis = TextBlob(text)
result = {"polarity": analysis.sentiment.polarity}

with open('/app/output.json', 'w') as f:
    json.dump(result, f)
