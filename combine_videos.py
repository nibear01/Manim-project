import subprocess
import os
import shutil

# Paths to generated scene videos (Manim output)
video_paths = [
    "media/videos/intro_video/1080p60/OpeningBranding.mp4",
    "media/videos/intro_video/1080p60/PersonalIntroduction.mp4",
    "media/videos/intro_video/1080p60/ClosingBranding.mp4"
]

# Paths to generated voiceovers
audio_paths = [
    "assets/audio/voiceover_opening.mp3",
    "assets/audio/voiceover_intro.mp3",
    "assets/audio/voiceover_closing.mp3"
]

# Temporary folder for intermediate files
temp_folder = "outputs/temp"
os.makedirs(temp_folder, exist_ok=True)

# Step 1: Merge each video with its corresponding audio
merged_videos = []
for i, (video, audio) in enumerate(zip(video_paths, audio_paths)):
    output_file = os.path.join(temp_folder, f"scene_{i+1}_merged.mp4")
    merged_videos.append(output_file)

    # FFmpeg command to merge video and audio, adjusting audio to video duration
    cmd = [
        "ffmpeg",
        "-i", os.path.abspath(video),
        "-i", os.path.abspath(audio),
        "-c:v", "copy",          # keep video codec
        "-c:a", "aac",           # convert audio to aac for mp4 compatibility
        "-map", "0:v:0",         # take video from first input
        "-map", "1:a:0",         # take audio from second input
        "-shortest",             # stop audio when video ends
        "-y",                    # overwrite if exists
        output_file
    ]
    print(f"Merging {video} with {audio} → {output_file}")
    subprocess.run(cmd, check=True)

# Step 2: Create a text file listing merged videos for concatenation
concat_file = os.path.join(temp_folder, "videos_to_concat.txt")
with open(concat_file, "w") as f:
    for mv in merged_videos:
        f.write(f"file '{os.path.abspath(mv).replace(os.sep, '/')}'\n")

# Step 3: Concatenate all merged videos into the final output
final_output = "outputs/videos/final_intro_video.mp4"
os.makedirs(os.path.dirname(final_output), exist_ok=True)

concat_cmd = [
    "ffmpeg",
    "-f", "concat",
    "-safe", "0",
    "-i", concat_file,
    "-c", "copy",
    "-y",
    final_output
]

print(f"Concatenating all scenes → {final_output}")
subprocess.run(concat_cmd, check=True)

# Step 4: Clean up temporary files
shutil.rmtree(temp_folder)

print("✅ Final video created successfully!")
