multimsg_md = """

# [MultiMsg插件](https://github.com/Zhalslar/astrbot_plugin_multimsg)
## 📦 安装

- 插件市场搜索multimsg安装
- 也可用git安装:

```bash
cd /AstrBot/data/plugins
git clone https://github.com/Zhalslar/astrbot_plugin_multimsg
```
### 命令表
|     命令       |       功能描述               |
| -------------- | ---------------------------- |
|  `md xxx`      |      发送markdown消息         |
|   `窥屏图片`    | 通过图片检测本群有谁在窥屏检测  |
"""


astrbot_md = """

# AstrBot

_✨ 易上手的多平台 LLM 聊天机器人及开发框架 ✨_

AstrBot 是一个开源的一站式 Agentic 聊天机器人平台及开发框架。

## ✨ 主要功能

1. **大模型对话**。支持接入多种大模型服务。支持多模态、工具调用、MCP、原生知识库、人设等功能。
2. **多消息平台支持**。支持接入 QQ、企业微信、微信公众号、飞书、Telegram、钉钉、Discord、KOOK 等平台。支持速率限制、白名单、百度内容审核。
3. **Agent**。完善适配的 Agentic 能力。支持多轮工具调用、内置沙盒代码执行器、网页搜索等功能。
4. **插件扩展**。深度优化的插件机制，支持[开发插件](https://astrbot.app/dev/plugin.html)扩展功能，社区插件生态丰富。
5. **WebUI**。可视化配置和管理机器人，功能齐全。

## ✨ 使用方式

#### Docker 部署

推荐使用 Docker / Docker Compose 方式部署 AstrBot。

请参阅官方文档 [使用 Docker 部署 AstrBot](https://astrbot.app/deploy/astrbot/docker.html#%E4%BD%BF%E7%94%A8-docker-%E9%83%A8%E7%BD%B2-astrbot) 。

#### 宝塔面板部署

AstrBot 与宝塔面板合作，已上架至宝塔面板。

请参阅官方文档 [宝塔面板部署](https://astrbot.app/deploy/astrbot/btpanel.html) 。

#### 1Panel 部署

AstrBot 已由 1Panel 官方上架至 1Panel 面板。

请参阅官方文档 [1Panel 部署](https://astrbot.app/deploy/astrbot/1panel.html) 。

#### 在 雨云 上部署

AstrBot 已由雨云官方上架至云应用平台，可一键部署。

[![Deploy on RainYun](https://rainyun-apps.cn-nb1.rains3.com/materials/deploy-on-rainyun-en.svg)](https://app.rainyun.com/apps/rca/store/5994?ref=NjU1ODg0)

#### 在 Replit 上部署

社区贡献的部署方式。

[![Run on Repl.it](https://repl.it/badge/github/Soulter/AstrBot)](https://repl.it/github/Soulter/AstrBot)

#### Windows 一键安装器部署

请参阅官方文档 [使用 Windows 一键安装器部署 AstrBot](https://astrbot.app/deploy/astrbot/windows.html) 。

#### CasaOS 部署

社区贡献的部署方式。

请参阅官方文档 [CasaOS 部署](https://astrbot.app/deploy/astrbot/casaos.html) 。

#### 手动部署

> 推荐使用 `uv`。

首先，安装 uv：

```bash
pip install uv
```

通过 Git Clone 安装 AstrBot：

```bash
git clone https://github.com/AstrBotDevs/AstrBot && cd AstrBot
uv run main.py
```

或者请参阅官方文档 [通过源码部署 AstrBot](https://astrbot.app/deploy/astrbot/cli.html) 。

## ⚡ 消息平台支持情况

| 平台    | 支持性 |
| -------- | ------- |
| QQ(官方机器人接口) | ✔    |
| QQ(OneBot)      | ✔    |
| Telegram   | ✔    |
| 企业微信    | ✔    |
| 微信客服    | ✔    |
| 微信公众号    | ✔    |
| 飞书   | ✔    |
| 钉钉   | ✔    |
| Slack   | ✔    |
| Discord   | ✔    |
| [KOOK](https://github.com/wuyan1003/astrbot_plugin_kook_adapter)   | ✔    |
| [VoceChat](https://github.com/HikariFroya/astrbot_plugin_vocechat)   | ✔    |
| 微信对话开放平台 | 🚧    |
| WhatsApp   | 🚧    |
| 小爱音响   | 🚧    |

## ⚡ 提供商支持情况

| 名称    | 支持性 | 类型 | 备注 |
| -------- | ------- | ------- | ------- |
| OpenAI API | ✔    | 文本生成 | 也支持 DeepSeek、Gemini、Kimi、xAI 等兼容 OpenAI API 的服务 |
| Claude API | ✔    | 文本生成 |  |
| Google Gemini API | ✔    | 文本生成 |  |
| Dify | ✔    | LLMOps |  |
| 阿里云百炼应用 | ✔    | LLMOps |  |
| Ollama | ✔    | 模型加载器 | 本地部署 DeepSeek、Llama 等开源语言模型 |
| LM Studio | ✔    | 模型加载器 | 本地部署 DeepSeek、Llama 等开源语言模型 |
| LLMTuner | ✔    | 模型加载器 | 本地加载 lora 等微调模型 |
| [优云智算](https://www.compshare.cn/?ytag=GPU_YY-gh_astrbot&referral_code=FV7DcGowN4hB5UuXKgpE74) | ✔    | 模型 API 及算力服务平台 |  |
| [302.AI](https://share.302.ai/rr1M3l) | ✔    | 模型 API 服务平台 |  |
| 硅基流动 | ✔    | 模型 API 服务平台 |  |
| PPIO 派欧云 | ✔    | 模型 API 服务平台 |  |
| OneAPI | ✔    | LLM 分发系统 |  |
| Whisper | ✔    | 语音转文本 | 支持 API、本地部署 |
| SenseVoice | ✔    | 语音转文本 | 本地部署 |
| OpenAI TTS API | ✔    | 文本转语音 |  |
| GSVI | ✔    | 文本转语音 | GPT-Sovits-Inference |
| GPT-SoVITs | ✔    | 文本转语音 | GPT-Sovits-Inference |
| FishAudio | ✔    | 文本转语音 | GPT-Sovits 作者参与的项目 |
| Edge TTS | ✔    | 文本转语音 | Edge 浏览器的免费 TTS |
| 阿里云百炼 TTS | ✔    | 文本转语音 |  |
| Azure TTS | ✔    | 文本转语音 | Microsoft Azure TTS |

## ❤️ 贡献

欢迎任何 Issues/Pull Requests！只需要将你的更改提交到此项目 ：)

### 如何贡献

你可以通过查看问题或帮助审核 PR（拉取请求）来贡献。任何问题或 PR 都欢迎参与，以促进社区贡献。当然，这些只是建议，你可以以任何方式进行贡献。对于新功能的添加，请先通过 Issue 讨论。

### 开发环境

AstrBot 使用 `ruff` 进行代码格式化和检查。

```bash
git clone https://github.com/Soulter/AstrBot
pip install pre-commit
pre-commit install
```

## 🌟 支持

- Star 这个项目！
- 在[爱发电](https://afdian.com/a/soulter)支持我！

## ✨ Demo

👉 点击展开多张 Demo 截图 👈

_✨基于 Docker 的沙箱化代码执行器（Beta 测试）✨_

_✨ 多模态、网页搜索、长文本转图片（可配置） ✨_

_✨ 插件系统——部分插件展示 ✨_

_✨ WebUI ✨_

## ❤️ Special Thanks

特别感谢[所有 Contributors 和插件开发者]("https://github.com/AstrBotDevs/AstrBot/graphs/contributors")对 AstrBot 的贡献 ❤️

此外，本项目的诞生离不开以下开源项目：

- [NapNeko/NapCatQQ](https://github.com/NapNeko/NapCatQQ) - 伟大的猫猫框架
- [wechatpy/wechatpy](https://github.com/wechatpy/wechatpy)

## ⭐ Star History

> [!TIP]
> 如果本项目对您的生活 / 工作产生了帮助，或者您关注本项目的未来发展，请给项目 Star，这是我维护这个开源项目的动力 <3

_私は、高性能ですから!_


"""
