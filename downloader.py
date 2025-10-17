import yt_dlp
import os
import sys

def download_video(url, output_path="downloads"):
    # Create downloads directory if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    # Enhanced download options
    ydl_opts = {
        'format': 'best[ext=mp4]/best',  # .MP4 format
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),  # Custom output template
        'noplaylist': True,  # Don't download playlists
        'extract_flat': False  # Extract full video info
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading video from: {url}")
            ydl.download([url])
            print("Download completed successfully!")
            
    except Exception as e:
        print(f"Error downloading video: {e}")
        return False
    
    return True

if __name__ == "__main__":
    print("YouTube Video Downloader")
    print("=" * 30)
    
    url = input("Enter YouTube URL: ").strip()
    
    if not url:
        print("No URL provided. Exiting...")
        sys.exit(1)
    
    success = download_video(url)
    
    if success:
        print("\n Video downloaded to 'downloads' folder!")
        print("You can now play the video using any media player.")
    else:
        print("\n Download failed. Please check the URL and try again.")