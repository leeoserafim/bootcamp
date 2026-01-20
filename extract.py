import pandas as pd
import requests
import json
link='https://jsonplaceholder.typicode.com/users'

df = pd.read_csv('/Users/leo/Documents/bootcamp/usuarios.csv')

user_ids = df['id'].tolist()
print(user_ids)

def get_user(id):
    
    url = f'https://jsonplaceholder.typicode.com/users/{id}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
users = [user for id in user_ids if (user := get_user(id)) if user is not None]
print(users)


