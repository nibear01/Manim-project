# Project Documentation

A professional **animated intro video pipeline** for **Imran’s Lab**, built with **Manim**, **gTTS**, and **FFmpeg**.  
This project combines **custom animations**, **narrated voiceovers**, and **automated video/audio merging** into one polished output.

---

## ✨ Features
- 🎨 Custom animations created with **Manim**  
- 🗣️ Text-to-speech narration using **gTTS**  
- 🎼 Automatic syncing of audio & video with **FFmpeg**  
- 📂 Modular design (easy to update narration, logo, or animations)  
- 🎥 Final high-quality **MP4 intro video**  

---

## 🛠️ Tools & Technologies Used
- **Python 3.13.3**  
- **[Manim](https://www.manim.community/)** (Mathematical Animation Engine)  
- **[gTTS](https://pypi.org/project/gTTS/)** (Google Text-to-Speech)  
- **[FFmpeg](https://ffmpeg.org/)** (Video & audio processing)  
- **NumPy** (for particle/random animations)  

---

## 🎬 Storyboard

### 🎥 Scene 1: Opening Branding
- **Background**: Light gradient rectangle with floating particles  
- **Elements**: Lab logo + slogan  
- **Animations**:  
  - Logo appears with scaling & rotation  
  - Slogan fades in with gradient effect  
  - Floating motion for logo & text  
- **Narration**:  
  *“Welcome to Imran’s Lab, inspiring minds, building futures...”*  

---

### 🎥 Scene 2: Personal Introduction
- **Background**: Expanding light-blue circles  
- **Elements**:  
  - “Hello! I’m Naved Abrar Nibir”  
  - “Fun fact: I love building web projects and exploring AI”  
  - “I’m studying at BRAC University”  
  - “Excited to join Imran’s Lab!”  
- **Animations**:  
  - Each text fades in with directional movement  
  - Floating animations for each text  
  - Rotating background circles  
- **Narration**: Personal introduction + highlights  

---

### 🎥 Scene 3: Closing Branding
- **Background**: Gradient with floating circles  
- **Elements**:  
  - “Thank you for watching!”  
  - “Stay curious and keep learning with Imran’s Lab”  
- **Animations**:  
  - Thank-you text fades in with scaling  
  - Closing slogan written on screen  
  - Gentle floating until fade-out  
- **Narration**: Motivational closing line  

---

## 📂 Project Structure
📂 ImransLabIntroVideo
│── intro_video.py # Manim animations
│── generate_voiceover.py # TTS generation with gTTS
│── combine_videos.py # FFmpeg merging + final video
│── narration_intro.txt # Narration script (3 sections)
│
📂 assets
│ ├── images
│ │ └── imranslab_logo.png
│ └── audio
│ ├── voiceover_opening.mp3
│ ├── voiceover_intro.mp3
│ └── voiceover_closing.mp3
│
📂 media (created by Manim during rendering)
📂 outputs
├── videos
│ └── final_intro_video.mp4
└── temp (temporary concat + merge files)


---

## ⚙️ Rendering Instructions

### 1️⃣ Install Dependencies
```bash
# Create virtual environment
python -m venv venv

# Activate venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install requirements
pip install manim gTTS
sudo apt install ffmpeg ```  # required for merging

2️⃣ Generate Animations
manim -pqh intro_video.py OpeningBranding
manim -pqh intro_video.py PersonalIntroduction
manim -pqh intro_video.py ClosingBranding


👉 Outputs will be saved in:
media/videos/intro_video/1080p60/

3️⃣ Generate Voiceovers
python generate_voiceover.py


👉 Creates:

assets/audio/voiceover_opening.mp3

assets/audio/voiceover_intro.mp3

assets/audio/voiceover_closing.mp3

4️⃣ Merge Video + Audio
python combine_videos.py


👉 Final video saved to:
outputs/videos/final_intro_video.mp4

👉 Final video saved to:
outputs/videos/final_intro_video.mp4


⚡ Challenges & Solutions
1. ⏱️ Syncing Animations with Voiceover

Problem: Text animations had fixed wait times, narration varied

Solution: Split narration into 3 scenes + used FFmpeg’s -shortest flag

2. 🎨 Making Animations Look Professional

Problem: Default fade-ins felt flat

Solution: Added particles, floating effects, and gradient text

3. 📂 Managing Multiple Files

Problem: Tracking 3 scenes + 3 voiceovers + merges

Solution: Automated pipeline with temp folder & concat file

4. 🖥️ Performance & Rendering Speed

Problem: High-quality Manim renders are slow

Solution: Used -pqh (preview high) for testing, -qh for final renders

🎯 Final Deliverable

✅ High-quality MP4 intro video: outputs/videos/final_intro_video.mp4

✅ Smooth animations synced with narration

✅ Consistent branding & modular design

✅ Easy to update narration, logo, or animation styles