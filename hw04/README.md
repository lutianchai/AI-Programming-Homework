# Homework 04: 大模型应用与语音技术综合实践

本目录包含了人工智能导论课程作业 **hw04** 的全部内容，涵盖了大模型文案生成、声音克隆以及开源语音识别（ASR）的调研与本地实现。

## 📁 目录结构

```text
hw04/
├── README.md               # 项目总体说明与导航
├── text_gen.md             # 任务一：大模型生成文案及 Prompt 说明
├── jianying.md             # 任务二：剪映声音克隆操作说明
├── audio/
│   └── cloned_voice.mp3    # 任务二：克隆后的配音音频文件
├── asr_report.md           # 任务三：ASR 调研对比报告与实验记录
├── asr_task.py             # 任务三：基于 Whisper 的 ASR 实现代码
└── requirements.txt        # Python 依赖环境清单
```

---

## 📝 任务完成情况说明

### 任务一：大模型生成文案
* **目标**：选定技术科普主题，利用 LLM 生成 200 字以上连贯文字。
* **内容**：详见 `text_gen.md`。
* **使用模型**：Gemini 3 Flash。

### 任务二：剪映声音克隆
* **目标**：利用剪映“克隆自己”功能，为任务一的文案进行配音。
* **产出**：音频文件已存放于 `audio/cloned_voice.mp3`。
* **说明**：在 `jianying.md` 中记录了具体的克隆步骤与导出参数。

### 任务三：开源语音识别 (ASR) 调研与实现
* **方案对比**：对比了 **OpenAI Whisper**、**Sherpa-ONNX** 和 **FunASR** 三种方案，从许可协议、推理速度及实测感受等维度进行了评估。
* **本地实现**：
    * 选用 **Whisper (Base)** 模型进行本地部署。
    * 实现了对任务二导出音频的自动识别转换。
* **运行方法**：
    ```bash
    pip install -r requirements.txt
    python asr_task.py
    ```
* **实验记录**：详见 `asr_report.md`。

---

## 🛠️ 环境要求
* **操作系统**：Windows 11 / macOS 13
* **运行环境**：Python 3.10+
* **硬件建议**：建议具备 GPU 环境以加速 Whisper 推理。

---

## 👨‍💻 提交信息
* **课程名称**：人工智能导论
* **作业编号**：hw04
* **仓库路径**：`/hw04/`

---
