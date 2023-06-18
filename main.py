import requests
import json
import time

print("Made by reviled#8182")

def check_username(username, password, webhook_url=None):
    url = "https://discord.com/api/v9/users/@me"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "OWN TOKEN",
    }
    data = {"username": username, "password": password}
    
    response = requests.patch(url, headers=headers, data=json.dumps(data))
    json_response = response.json()
    
    if webhook_url:
        if 'errors' in json_response:
            if 'username' in json_response['errors']:
                message = f"``❌ Username {username} is not working.``"
            else:
                message = f"``✔️ Username {username} is free.``"
                send_webhook_notification(webhook_url2, message)
        else:
            message = f"Error occurred while checking username {username}."
            send_webhook_notification(webhook_url, message)
        
    
    return json_response

def send_webhook_notification(webhook_url, message):
    data = {
        "content": message
    }
    response = requests.post(webhook_url, json=data)
    if response.status_code != 204:
        print("Failed to send webhook notification.")

def process_usernames(file_path, delay=60/20, webhook_url=None):
    with open(file_path, 'r') as file:
        usernames = file.read().splitlines()

    for username in usernames:
        password = "" # Keep empty until you want to snipe the username.
        response = check_username(username, password, webhook_url)
        
        if 'errors' in response:
            if 'username' in response['errors']:
                print(f"Username {username} is unavailable.")
            else:
                print(f"Username {username} is free.")
        
        time.sleep(delay)

# Specify your file path and webhook URL here
file_path = 'users.txt'
webhook_url = 'INVALID WEBHOOK CHANNEL'
webhook_url2 = 'VALID WEBHOOK CHANNEL'

process_usernames(file_path, webhook_url=webhook_url)
