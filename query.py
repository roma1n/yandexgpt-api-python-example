import os
import requests

IAM_TOKEN = os.getenv('IAM_TOKEN')
FOLDER_ID = os.getenv('FOLDER_ID')
API_URL = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'
PROMPT = {
  'modelUri': 'gpt://{}/yandexgpt-lite'.format(FOLDER_ID),
  'completionOptions': {
    'stream': False,
    'temperature': 0.6,
    'maxTokens': '2000'
  },
  'messages': [
    {
      'role': 'system',
      'text': 'Найди ошибки в тексте и исправь их'
    },
    {
      'role': 'user',
      'text': 'Ламинат подойдет для укладке на кухне или в детской комнате – он не боиться влаги и механических повреждений благодаря защитному слою из облицованных меламиновых пленок толщиной 0,2 мм и обработанным воском замкам.'
    }
  ]
}

r = requests.post(
    API_URL,
    headers={
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {IAM_TOKEN}',
        'x-folder-id': FOLDER_ID,
    },
    json=PROMPT,
)

print(r.text)
