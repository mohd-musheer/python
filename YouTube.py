import yt_dlp

def download_video(video_url):
    try:
        # Fetch available video streams
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(video_url, download=False)
        
        print(f"\nTitle: {info['title']}\n")
        print("Available Resolutions:")
        
        # List available video resolutions
        video_streams = [
            f"{stream['format_id']} - {stream['format_note']} ({stream['ext']})"
            for stream in info['formats']
            if stream['vcodec'] != 'none' and stream['acodec'] != 'none'
        ]
        
        for i, stream in enumerate(video_streams, start=1):
            print(f"{i}. {stream}")
        
        # Get user's choice
        choice = int(input("\nEnter the number of your preferred resolution: ")) - 1
        selected_format = info['formats'][choice]
        
        print(f"\nDownloading: {selected_format['format_note']} resolution...")
        
        # Download the selected format
        ydl_opts = {
            'format': selected_format['format_id'],  # Use selected format ID
            'outtmpl': '%(title)s.%(ext)s',         # Save file as video title
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        
        print("Download completed!")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Enter the YouTube video URL
video_url = input("Enter YouTube video URL: ")
download_video(video_url)

