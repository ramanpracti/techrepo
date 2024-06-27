import requests
import json

# API AUTH
username = ""
token = ""



add_url = 'https://.atlassian.net/rest/api/2/field/'

am_headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

payload = json.dumps(
    {
    "name": "GitHub for practiproject",
    "description": "This is a custom field for my project",
    "type": "com.atlassian.jira.plugin.system.customfieldtypes:textfield"
}
)


am_response = requests.request(
        "POST",
        add_url,
        data=payload,
        headers=am_headers,
        auth=(username, token)
    )

