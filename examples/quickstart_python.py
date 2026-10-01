"""ChatPort quickstart — Python (OpenAI SDK)."""
from openai import OpenAI

client = OpenAI(
    api_key="你的 ChatPort Key",          # 从 https://admin.chatport.top/console 获取
    base_url="https://api.chatport.top/v1",  # 只改这一行
)

resp = client.chat.completions.create(
    model="deepseek-chat",  # 或 deepseek-reasoner / gpt-4o-mini / gpt-6-astra …
    messages=[
        {"role": "system", "content": "你是一个简洁的助手。"},
        {"role": "user", "content": "用一句话介绍你自己。"},
    ],
)
print(resp.choices[0].message.content)
