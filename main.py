import pandas as pd
from datetime import datetime
import openai

TODAY_DATE = datetime.today()
data_today_string = TODAY_DATE.strftime("%d/%m")

df = pd.read_excel("SDW2023.xlsx")

users_id = df['ID'].tolist()

user = {}

user_birthday_1 = df['BIRTHDAY'].tolist()
user_birthday = [birthday_[0:5] for birthday_ in user_birthday_1]

user_name = df['NAME'].tolist()

for i, (name, birthday) in enumerate(zip(user_name, user_birthday), start=1):
    user_id = f"id{i}"
    user[user_id] = {'name': name, 'birthday': birthday, 'news': []}

openai_api_key = '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'
openai.api_key = openai_api_key


def generate_ai_news(name):
    prompt = f"Você é gerente do banco Santander.\n"
    prompt += f"Crie uma mensagem para {name} o parabenizando pelo seu aniversário (máximo de 100 caracteres)\n"

    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    return completion.choices[0].text.strip('\"')

news_list = []

for user_id, user_data in user.items():
    if user_data['birthday'] == data_today_string:
        news = generate_ai_news(user_data)
        news_list.append(news)

for news in news_list:
    print(news)
