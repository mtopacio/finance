import requests
import json

url="https://discord.com/api/webhooks/1124247295618187345/Z04YvBzEaR_rtvU_cXn7IXv3-mXui3WnqG6HqoHkWWk-uYwZwU-0oZjgQOhyCTBmPhV-"

data = json.dumps({
    "content": "This is the message content."
})
print(data)

resp = requests.post(url, data=data, headers={"Content-Type": "application/json"})
print(resp)
