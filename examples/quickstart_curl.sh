#!/usr/bin/env bash
# ChatPort quickstart — curl
# 把 YOUR_KEY 换成从 https://admin.chatport.top/console 获取的 Key
curl https://api.chatport.top/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_KEY" \
  -d '{
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": "用一句话介绍你自己。"}]
  }'
