#!/usr/bin/env python3

import json

# reading file into python
with open('schacon.repos.json', 'r') as file:
    data = json.load(file)

# create a list
repos = []

# we want first 5
for d in data[:5]:
    # getting specific fields
    name = d["name"]
    html_url = d["html_url"]
    updated_at = d["updated_at"]
    visibility = d["visibility"]

# Assemble into comma-separated line
    line = name + "," + html_url + "," + updated_at + "," + visibility + "\n"

    # Append line to repos list
    repos.append(line)

# Write lines to chacon.csv
with open("chacon.csv", "a") as csv:
    csv.writelines(repos)
