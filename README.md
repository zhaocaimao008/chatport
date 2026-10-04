# ChatPort API — OpenAI 兼容接口中转

标准 OpenAI 兼容接口，现有代码**只改一行 `base_url`** 就能用。

- **DeepSeek**：`deepseek-chat`（V3）、`deepseek-reasoner`（R1）
- **OpenAI**：`gpt-4o` / `gpt-4o-mini` / `gpt-4.1` 系列、`gpt-6-astra`、`gpt-6.1-sol`

## 快速开始

```python
from openai import OpenAI

client = OpenAI(
    api_key="你的 ChatPort Key",
    base_url="https://api.chatport.top/v1",
)

resp = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "你好"}],
)
print(resp.choices[0].message.content)
```

更多示例见 [`examples/`](./examples)（Node.js、curl、LangChain）。

## 获取 Key

1. 注册：https://admin.chatport.top/register
2. 控制台自助创建 Key
3. 充值：https://api.chatport.top/pay/（最低 ¥10）

## 计费

按量计费，无月租，全系官方价 ×1.3。充值汇率 ¥7.2 = $1 额度：

| 模型 | 输入 / 百万 token | 输出 / 百万 token |
| ---- | ---- | ---- |
| deepseek-chat | $0.35 | $1.43 |
| deepseek-reasoner | $0.72 | $2.85 |
| gpt-4o-mini | $0.20 | $0.78 |
| gpt-6.1-sol | $2.60 | $13.00 |
| gpt-4o | $3.25 | $13.00 |
| gpt-6-astra | $13.00 | $65.00 |

新用户注册送 $2 额度。

## 链接

- 官网 / 文档：https://api.chatport.top
- 充值：https://api.chatport.top/pay/
- YouTube：https://www.youtube.com/@ChatPort

个人运营，上游为官方渠道。问题反馈请提 Issue。
