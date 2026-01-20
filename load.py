from extract import users,link
import json
import requests as request

def update_user(user):
    response = request.put(f"{link}/{user['id']}", json=user)
    return True if response.status_code == 200 else False

for user in users:
    success = update_user(user)
    print(f"User {user['id']} update {'succeeded' if success else 'failed'}")   