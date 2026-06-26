import requests
import os

# Your Supadata API key
API_KEY = "sd_43b921ae23d7e59979d4b4a9dbe3ddad"

# Real YouTube videos from our experts
videos = {
    "jason-bay": [
        "DAz7BegV-RE",
        "LEzzJjCHGC4",
    ],
    "alex-berman": [
        "TcNf03BmS44",
        "hatrtJIncLc",
    ],
    "patrick-dang": [
        "leseMonDxB4",
        "p1lR_cyPnSE",
    ],
    "jack-reamer": [
        "gNOkEHW8VSE",
        "J9qOjPhSW9o",
    ],
}

for expert, video_ids in videos.items():
    folder = f"research/youtube-transcripts/{expert}"
    os.makedirs(folder, exist_ok=True)

    for i, video_id in enumerate(video_ids):
        print(f"Fetching transcript for {expert} - video {i+1}...")
        try:
            url = "https://api.supadata.ai/v1/youtube/transcript"
            params = {"videoId": video_id}
            headers = {"x-api-key": API_KEY}
            response = requests.get(url, params=params, headers=headers)
            data = response.json()

            if "content" in data:
                text = " ".join([seg["text"] for seg in data["content"]])
                filename = f"{folder}/video-{i+1}.md"
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(f"# Transcript\n")
                    f.write(f"**Expert:** {expert}\n")
                    f.write(f"**Source:** https://www.youtube.com/watch?v={video_id}\n\n")
                    f.write("---\n\n")
                    f.write(text)
                print(f"  Saved: {filename}")
            else:
                print(f"  No transcript: {data}")
        except Exception as e:
            print(f"  Error: {e}")

print("\nAll done!")