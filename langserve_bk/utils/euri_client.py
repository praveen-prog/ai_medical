import requests

API_KEY='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI1MTdhM2FkYS1jMWRjLTRlNzItYjA3My05MjUxMTE3ZmU3MzciLCJlbWFpbCI6InByYXZlZW5tZWtAZ21haWwuY29tIiwiaWF0IjoxNzQxOTY5MjUyLCJleHAiOjE3NzM1MDUyNTJ9.HFSoboyUM4GSbRsAa2dBDf_AWd44Qoo7dRQ-nhk8AA4'
BASE_URL="https://api.euron.one/api/v1/euri/alpha/chat/completions"

def euri_chat_completion(messages,temperature=0.7,max_tokens=1000):
    url = "https://api.euron.one/api/v1/euri/alpha/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI1MTdhM2FkYS1jMWRjLTRlNzItYjA3My05MjUxMTE3ZmU3MzciLCJlbWFpbCI6InByYXZlZW5tZWtAZ21haWwuY29tIiwiaWF0IjoxNzQ1MjcyNTAzLCJleHAiOjE3NzY4MDg1MDN9.lEGOq-4nNiZzXMdKZbCPaSWNVhPtP4v9w1Rqzhz-EWc"
    }
    payload = {
        "messages": messages,
        "model": "gpt-4.1-nano",
        "max_tokens": max_tokens,
        "temperature": temperature
    }

    response = requests.post(url, headers=headers, json=payload)    
    return response.json()["choices"][0]["message"]["content"]


