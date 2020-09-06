from django.shortcuts import render
from django.http import HttpResponse
from .services.downloader import Downloader
import json

# Create your views here.
def video(request):
    if request.method == 'POST':
        req_body = dict(request.POST)
        downloader = Downloader()
        downloader.set_single_video_link(str(req_body['link']))
        res_body = dict()
        res_body["link"] = req_body["link"][0]
        res_body["title"] = downloader.get_video_title()
        res_body["available_links"] = [(i.mime_type, i.resolution) for i in downloader.get_available_video_streams()]
        res_body['thumbnail'] = downloader.get_video_thumbnail()
        return render(request, 'downloader/video.html', {'data': res_body})
    return render(request, 'downloader/video.html')

def music(request):
    if request.method == 'POST':
        req_body = dict(request.POST)
        downloader = Downloader()
        downloader.set_single_video_link(str(req_body['link']))
        res_body = dict()
        res_body["link"] = req_body["link"][0]
        res_body["title"] = downloader.get_video_title()
        res_body["available_links"] = [(i.mime_type, i.resolution) for i in downloader.get_available_audio_streams()]
        res_body['thumbnail'] = downloader.get_video_thumbnail()
        return render(request, 'downloader/music.html', {'data': res_body})
    return render(request, 'downloader/music.html')

def playlist(request):
    if request.method == 'POST':
        req_body = dict(request.POST)
        downloader = Downloader()
        downloader.set_playlist_link(str(req_body['link']))
        res_body = dict()
        res_body["link"] = req_body["link"][0]
        res_body["playlist_contents"] = downloader.get_playlist_videos()
        return render(request, 'downloader/playlist.html', {'data': res_body})
    return render(request, 'downloader/playlist.html')