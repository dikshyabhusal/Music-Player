import re
import json

# Input: Replace this with syncedlyrics output
query = input("Enter Song Name: ")
lrc = syncedlyrics.search(query)

# Process synced lyrics
lines = lrc.split('\n')
pattern = r'\[(\d+:\d+\.\d+)\] (.+)'
json_data = []

for line in lines:
    match = re.match(pattern, line)
    if match:
        timestamp, text = match.groups()
        json_data.append({"time": timestamp, "lyrics": text})

# Output the JSON
json_string = json.dumps(json_data, indent=4)
print(json_string)
