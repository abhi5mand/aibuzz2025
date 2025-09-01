import sounddevice as sd
import numpy as np
import queue
import time
import argparse
from qai_hub_models.models.yamnet.app import YamNetApp
from qai_hub_models.models.yamnet.model import MODEL_ID, YamNet
from qai_hub_models.utils.asset_loaders import qaihm_temp_dir
from qai_hub_models.utils.args import get_model_cli_parser, get_on_device_demo_parser, demo_model_from_cli_args
import soundfile as sf
from pathlib import Path

# Audio settings
SAMPLE_RATE = 16000
BUFFER_DURATION = 2
BUFFER_SIZE = SAMPLE_RATE * BUFFER_DURATION

# Thread-safe queue
audio_queue = queue.Queue()

# Simulate CLI args
parser = get_model_cli_parser(YamNet)
parser = get_on_device_demo_parser(parser, add_output_dir=False)
args = parser.parse_args([])

# Load model using simulated args
model = demo_model_from_cli_args(YamNet, MODEL_ID, args)
app = YamNetApp(model)

# Callback to collect audio
def audio_callback(indata, frames, time_info, status):
    if status:
        print(status)
    audio_queue.put(indata.copy())

# Process audio chunks
def process_audio():
    buffer = np.empty((0, 1), dtype=np.float32)
    print("\n🎙️ Starting live audio classification... Press Ctrl+C to stop.")
    try:
        while True:
            chunk = audio_queue.get()
            buffer = np.concatenate((buffer, chunk))
            if len(buffer) >= BUFFER_SIZE:
                audio_chunk = buffer[:BUFFER_SIZE]
                buffer = buffer[BUFFER_SIZE:]

                with qaihm_temp_dir() as tmpdir:
                    temp_path = Path(tmpdir) / "live.wav"
                    sf.write(temp_path, audio_chunk, SAMPLE_RATE)
                    predictions = app.predict(path=str(temp_path))

                top5_classes = " | ".join(predictions)
                print(f"🔍 Top 5 predictions: {top5_classes}")
    except KeyboardInterrupt:
        print("\n🛑 Stopped live classification.")

# Start stream
stream = sd.InputStream(samplerate=SAMPLE_RATE, channels=1, callback=audio_callback)
with stream:
    process_audio()




