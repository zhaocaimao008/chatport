// ChatPort quickstart — Node.js (openai SDK)
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "你的 ChatPort Key", // 从 https://admin.chatport.top/console 获取
  baseURL: "https://api.chatport.top/v1", // 只改这一行
});

const resp = await client.chat.completions.create({
  model: "gpt-4o-mini", // 或 deepseek-chat / gpt-6-astra …
  messages: [{ role: "user", content: "用一句话介绍你自己。" }],
});

console.log(resp.choices[0].message.content);
