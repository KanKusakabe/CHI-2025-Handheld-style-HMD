import os
import subprocess

# movファイルがあるディレクトリを指定
MOV_DIR = "."

# gifファイルを保存するディレクトリ（同じディレクトリに保存）
GIF_DIR = "."

# GIFの幅を指定（高さは自動調整）
GIF_WIDTH = 800

# フレームレートを指定
FRAME_RATE = 30

# movファイルを探索して変換
for filename in os.listdir(MOV_DIR):
    if filename.lower().endswith(".mov"):
        mov_path = os.path.join(MOV_DIR, filename)
        gif_filename = f"{os.path.splitext(filename)[0]}.gif"
        gif_path = os.path.join(GIF_DIR, gif_filename)

        # ffmpegコマンドでmovをgifに変換
        command = [
            "ffmpeg",
            "-i", mov_path,
            "-vf", f"scale={GIF_WIDTH}:-1",
            "-r", str(FRAME_RATE),
            gif_path
        ]

        print(f"Converting {mov_path} to {gif_path}...")
        subprocess.run(command)

print("All mov files converted to gif.")
