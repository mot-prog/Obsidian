---
tags:
  - ffmpeg
  - cli
  - video
  - media
  - linux
aliases:
  - Extract thumbnail from video
  - FFmpeg screenshot
---
## Affiche les détails de n'importe quel media
```bahs
mediainfo fichier.mp3
```
## Extract a Thumbnail from a Video using FFmpeg

This command extracts a single frame (image) from a video file at a specific timestamp to serve as a thumbnail.

### The Command

```bash
ffmpeg -i <input_video_path> -ss <timestamp> -vframes 1 <output_image_path>
````

> [!example] Specific Example
> ```Bash
> ffmpeg -i media/videos/smolvla_16000.mp4 -ss 00:00:02.000 -vframes 1 media/pictures/thumbnails/smolvla_16000.png
> ```

### Parameter Breakdown

- **`-i <input_video_path>`**: Specifies the input video file path.
    
- **`-ss <timestamp>`**: Seeks to the specific timestamp (e.g., `00:00:02.000` for exactly 2 seconds into the video).
    
- **`-vframes 1`**: Instructs FFmpeg to output exactly one video frame.
    
- **`<output_image_path>`**: The destination file. FFmpeg automatically determines the output image format based on the file extension (e.g., `.png`).