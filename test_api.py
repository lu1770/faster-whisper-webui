try:
  import requests
except:
  import pip
  pip.main(['install', 'requests'])

import json
import requests

    # simple_inputs = lambda : [
    #     gr.Dropdown(choices=whisper_models, value=app_config.default_model_name, label="Model/模型"),
    #     gr.Dropdown(choices=sorted(get_language_names()), label="Language/语言(为空时自动识别)", value=app_config.language),
    #     gr.Text(label="URL (YouTube, etc.)/链接(YouTube,其他)"),
    #     gr.File(label="Upload Files/上传文件", file_count="multiple"),
    #     gr.Audio(source="microphone", type="filepath", label="Microphone Input/麦克风输入"),
    #     gr.Dropdown(choices=["transcribe", "translate"], label="Task/任务", value=app_config.task),
    #     gr.Dropdown(choices=["none", "silero-vad", "silero-vad-skip-gaps", "silero-vad-expand-into-gaps", "periodic-vad"], value=app_config.default_vad, label="VAD/语音活性检测"),
    #     gr.Number(label="VAD - Merge Window (s)/VAD - 合并窗口（秒）", precision=0, value=app_config.vad_merge_window),
    #     gr.Number(label="VAD - Max Merge Size (s)/VAD - 最大合并大小（秒）", precision=0, value=app_config.vad_max_merge_size),
    #     gr.Number(label="VAD - Padding (s)/VAD - 填充（秒）", precision=None, value=app_config.vad_padding),
    #     gr.Number(label="VAD - Prompt Window (s)/VAD - 提示窗口（秒）", precision=None, value=app_config.vad_prompt_window),
    # ]
model_name = "medium"
lang = "Chinese"
url = "https://www.bilibili.com/video/BV1Zh4y117Kt/?share_source=copy_web&vd_source=18115785651ee4735ae944b26ba25b66"
upload_files = {"name":"zip.zip","data":"data:@file/octet-stream;base64,UEsFBgAAAAAAAAAAAAAAAAAAAAAAAA=="}
upload_files = None
microphone = {"name":"audio.wav","data":"data:audio/wav;base64,UklGRiQAAABXQVZFZm10IBAAAAABAAEARKwAAIhYAQACABAAZGF0YQAAAAA="}
microphone = None
task_name = "transcribe"
vad = "silero-vad"
var_merge_window = 5
vad_max_merge_size = 30
vad_padding = 1
vad_prompt_window = 3
response = requests.post("http://127.0.0.1:17860/run/predict", json={
	"data": [
		model_name,
		lang,
		url,
		upload_files,
		microphone,
		task_name,
		vad,
		var_merge_window,
		vad_max_merge_size,
		vad_padding,
		vad_prompt_window,
	]
}).json()
print(json.dumps(response, indent=2))
data = response["data"]