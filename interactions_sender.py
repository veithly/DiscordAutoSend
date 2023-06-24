import argparse
import json
import os

import requests

import notify

url = "https://discord.com/api/v9/interactions"
authorization = os.environ.get('discord_authorization')
parser = argparse.ArgumentParser()

json_path = parser.add_argument('--json', type=str, help='json file path')

payload_list = json.load(open(parser.parse_args().json, 'r'))

headers = {
    'authority': 'discord.com',
    'authorization': authorization,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
}

msg = ""

for payload in payload_list:
    try:
        response = requests.request("POST", url, headers=headers, json=payload)
        msg += f"Send {payload['data']['name']} to {payload['channel_id']} with status code {response.status_code}\n"
    except Exception as e:
        msg += f"Error occured while sending {payload['data']['name']} to {payload['channel_id']}\n"
        msg += f"Error: {e}\n"

notify.send("===Discord Interaction Sender===", msg)
