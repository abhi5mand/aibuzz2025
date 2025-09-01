
# AI Buzz Phase 2 Submission

## Idea Details
- Team Name: WorkSafeRoute
- Idea Title: AI on the Fast Track - Smarter Roads for Emergency Response
- Idea url: NA
- Team Members
  - Sourabh Banerjee
  - Neeraj Vishwakarma
  - Abhijeet Mandloi
- Programming language used: Python
- AI Hub Model links
  - YamNet - https://aihub.qualcomm.com/models/yamnet?searchTerm=yamnet
  - [YOLOv8 - Object Detection](https://aihub.qualcomm.com/models/yolov8)
  - PoseNet - Pose Estimation
- Target device
  -  Qualcomm RB3GEN2

## Implementation Summary
This project aims to improve emergency response efficiency by enabling traffic systems to detect and respond to emergency vehicles in real-time. It uses:
- **YamNet** for detecting sirens from live audio.
- **YOLOv8** for identifying emergency vehicles in video feeds.

The system makes decisions based on a weighted consensus of audio and visual inputs to adjust traffic signals and notify neighboring junctions.

Important files:
- `detect_live_audio.py`: Live siren detection using YamNet.

Limitations:
- Real-time integration with traffic infrastructure is pending.
- Accuracy depends on environmental noise and camera quality.

Future Scope:
- Integration with smart traffic lights.
- Expansion to mobile platforms.

## Installation & Setup steps
Note: Make sure you have sudo access on the device.
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows use venv\Scriptsctivate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Run the live audio detection script
python detect_live_audio.py
```

## Expected output / behaviour
- The system continuously listens for sirens and identifies emergency vehicles.
- When a siren is detected, it prints the top 5 predictions.

## Next Work Items
- As this is just a prototype , we will enhance this appliaction to include yolov8 model to detect emergency vehicles.
- Once this is done both models output can be used to make predictions/decisions
- Once above steps are validated, the system can trigger traffic signal adjustments and notify nearby junctions and can also generate reports to send to concern deparments.


