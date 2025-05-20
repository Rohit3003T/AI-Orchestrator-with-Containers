import json
with open('/app/input.json') as f:
    data = json.load(f)

# Very basic clean: remove empty strings
cleaned = [x for x in data if x]

with open('/app/output.json', 'w') as f:
    json.dump(cleaned, f)
