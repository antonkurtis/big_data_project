import pandas as pd
import requests

def get_avg_salary():
    url = 'https://gogov.ru/articles/average-salary'
    headers = requests.utils.default_headers()

    headers.update(
        {
            'User-Agent': 'My User Agent 1.0',
        }
    )
    response = requests.get(url, headers=headers)

    df_list = pd.read_html(response.text)
    df = df_list[0]

    df.to_csv('data/avg_salary.csv', index=False)
