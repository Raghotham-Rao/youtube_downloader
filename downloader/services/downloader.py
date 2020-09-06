from pytube import YouTube, Playlist


class Downloader:

    def __init__(self):
        pass

    def set_single_video_link(self, link):
        self.yt = YouTube(link)

    def get_video_title(self):
        return self.yt.title
    
    def get_video_thumbnail(self):
        return self.yt.thumbnail_url
    
    def get_available_video_streams(self):
        return self.yt.streams.filter(only_video=True)

    def get_available_audio_streams(self):
        return self.yt.streams.filter(only_audio=True)

    def download_single_video(self, stream_index: int, audio_only=False):
        if audio_only:
            self.yt.streams.filter(only_audio=True)[stream_index]
        self.yt.streams[stream_index].download()

    def set_playlist_link(self, link):
        self.playlist = Playlist(link)
        
    def get_playlist_videos(self):
        return self.playlist.video_urls()

    def download_playlist(self):
        self.playlist.download_all()

    # TO BE STUDIED AND DEVELOPED
    # def get_subtitles(self):
    #     return self.yt.captions.all()