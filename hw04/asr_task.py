import whisper
import os

def run_asr(audio_path):
    # 1. 加载模型 (建议选 base 或 small 兼顾速度与准确度)
    model = whisper.load_model("base")
    
    print(f"正在识别音频: {audio_path} ...")
    
    # 2. 进行识别
    result = model.transcribe(audio_path, initial_prompt="以下是关于AI语音克隆的科普。")
    
    # 3. 输出结果
    print("-" * 20)
    print("识别结果：")
    print(result["text"])
    print("-" * 20)
    
    return result["text"]

if __name__ == "__main__":
    # 确保你把剪映导出的音频放在这里，或者改名为 output.mp3
    path = "output.mp3" 
    if os.path.exists(path):
        run_asr(path)
    else:
        print("请先将任务二导出的音频文件命名为 output.mp3 并放在当前目录。")
