import openai
import pandas as pd
from extract import get_user, users, user_ids,df
openai_api_key = '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'
openai.api_key = openai_api_key




def generate_ai_news(user):
    completion = openai.chat.completions.create(
        model="gpt-4o",  
        messages=[
            {
                "role": "developer",
                "content": "Voce é um especialista em marketing de uma empresa que vende camisetas de motovelicidade chamada RevRiders."
            },
            {
                "role": "user",
                "content": f'Crie uma mensagem de marketing de lançamento da marca RevRiders para um usuario chamado {user["name"]}. A mensagem deve ser curta, envolvente e incluir uma chamada para ação para visitar nosso site e conferir a nova coleção de camisetas.(a mensagem deve ter no maximo 100 caracteres) '
            }
        ]
    )
    return completion.choices[0].message.content.strip('\"')

for user in users:
    news = generate_ai_news(user)
    print(news)
    user['news'].append({
            "description": news
        })