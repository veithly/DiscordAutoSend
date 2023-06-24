# DiscordAutoSend

## Description

The script automatically sends instructions to the Discord robot to perform check-in and punch-in tasks.

## Usage

1. Configure environment variables for message publishing.

```bash
export BARK_PUSH=your_bark_push_key
...
```

2. Configure the Discord identity key for the environment variable.

```bash
export discord_authorization=your_discord_authorization
```

3. The corresponding instructions are stored as JSON files in directory.

```json
[
  {
    "type": 2,
    "application_id": "159985415099514880",
    "guild_id": "898153438217633862",
    "channel_id": "962932......",
    "session_id": "7ce5b64e6b5a5b2......",
    "data": {
      "version": "1036965985858617437",
      "id": "940112581509644326",
      "guild_id": "898153438217633862",
      "name": "work",
      "type": 1,
      "options": [],
      "application_command": {
        "id": "9401125815......",
        "application_id": "159985415099514880",
        "version": "1036965985858617437",
        "default_member_permissions": "2147483648",
        "type": 1,
        "nsfw": false,
        "name": "work",
        "description": "Work for one hour and come back to claim your paycheck",
        "guild_id": "898153438217633862",
        "options": [
          {
            "type": 3,
            "name": "action",
            "description": "Optional action like claim"
          }
        ]
      },
      "attachments": []
    },
    "nonce": "1122010556534882304"
  },
  {
    "type": 2,
    "application_id": "159985415099514880",
    "guild_id": "966518193214607370",
    "channel_id": "999051......",
    "session_id": "f76a6db1824a90a......",
    "data": {
      "version": "1001734770616717396",
      "id": "1001734770071441432",
      "guild_id": "966518193214607370",
      "name": "work",
      "type": 1,
      "options": [],
      "application_command": {
        "id": "100173477......",
        "application_id": "159985415099514880",
        "version": "1001734770616717396",
        "default_member_permissions": "2147483648",
        "type": 1,
        "nsfw": false,
        "name": "work",
        "description": "Work for one hour and come back to claim your paycheck",
        "guild_id": "966518193214607370",
        "options": [
          {
            "type": 3,
            "name": "action",
            "description": "Optional action like claim"
          }
        ]
      },
      "attachments": []
    },
    "nonce": "1122073759608471552"
  }
]
```

4. Run the script.

```bash
python3 interactions_sender.py --json your_json_file.json
```