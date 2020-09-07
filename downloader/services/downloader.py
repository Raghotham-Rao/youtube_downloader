from pytube import YouTube, Playlist
import re


class Downloader:

    def __init__(self):
        pass

    def set_single_video_link(self, link):
        self.yt = YouTube(link)

    def get_title(self, is_playlist=False):
        return self.playlist.title if is_playlist else self.yt.title

    def get_playlist_title(self):
        return self.playlist.title
    
    def get_video_thumbnail(self):
        return self.yt.thumbnail_url
    
    def get_available_video_streams(self):
        return self.yt.streams.filter(only_video=True)

    def get_available_audio_streams(self):
        return self.yt.streams.filter(only_audio=True)

    def download_single_video(self, stream_index: int, audio_only=False):
        if audio_only:
            self.yt.streams.filter(only_audio=True)[stream_index].download('media/')
        self.yt.streams[stream_index].download('media/')

    def set_playlist_link(self, link):
        self.playlist = Playlist(link)
        
    def get_playlist_videos(self):
        # print(self.playlist.videos)
        return [i for i in self.playlist.videos]

    def download_playlist(self):
        self.playlist.download_all()

    # TO BE STUDIED AND DEVELOPED
    # def get_subtitles(self):
    #     return self.yt.captions.all()

# downloader = Downloader()
# downloader.set_playlist_link('https://www.youtube.com/watch?v=Edpy1szoG80&list=PL153hDY-y1E00uQtCVCVC8xJ25TYX8yPU')
# # print(downloader.get_title(is_playlist=True))
# for i in downloader.playlist.videos:
#     print(i)