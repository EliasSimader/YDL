# YDL — YouTube Video Downloader

Simple Python script to download YouTube videos to your computer in .mp4 when possible. Saves files into a `downloads` folder next to the script.

### Features
- Downloads single YouTube videos (no playlists)
- Tries to save as `.mp4` for broad compatibility
- Creates a `downloads` folder automatically

## Requirements
- **Python**: 3.8+ recommended
- **yt-dlp**: `pip install yt-dlp`
- **FFmpeg**: Required so yt-dlp can merge/remux streams into a single playable file
  - Windows: Download a release from `https://www.gyan.dev/ffmpeg/builds/` or `https://www.ffmpeg.org/`
  - Add the `bin` folder (containing `ffmpeg.exe`) to your system `PATH`

## Install
```bash
pip install yt-dlp
```

Install FFmpeg and ensure `ffmpeg` is available in your terminal (`ffmpeg -version` should work).

## Usage (CLI)
```bash
python downloader.py
```
When prompted, paste a YouTube video URL. The video will be downloaded into the `downloads` directory.

Default behavior:
- Format: best available, preferring `.mp4`
- Output path: `./downloads/%(title)s.%(ext)s`
- Playlists: disabled (single video only)

## Programmatic usage (optional)
You can also call the downloader from Python code:
```python
from downloader import download_video

download_video("https://www.youtube.com/watch?v=VIDEO_ID", output_path="my_downloads")
```

## Media player compatibility
- On Windows, the default Windows Media Player may fail to play some downloaded files due to missing codecs.
- **Recommendation**: Use **VLC media player** (`https://www.videolan.org/vlc/`) which supports a wide range of codecs out of the box.

## Notes on FFmpeg
- yt-dlp relies on FFmpeg to:
  - Merge separate audio/video streams
  - Remux into `.mp4` when possible
- If FFmpeg is not installed or not in `PATH`, downloads may fail or produce files some players cannot open.

## Troubleshooting
- "ffmpeg not found" or merging errors: install FFmpeg and ensure `ffmpeg -version` works in your terminal.
- Video plays in VLC but not in Windows Media Player: this is expected for some encodings; use VLC.
- Very large or unusual formats: try a different YouTube quality or ensure FFmpeg is up to date.
- Update yt-dlp when downloads break: `python -m pip install -U yt-dlp`

## Legal
Respect YouTube Terms of Service and copyright laws. Only download content you have rights to or permission to use.