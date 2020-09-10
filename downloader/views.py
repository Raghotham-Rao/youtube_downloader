from django.shortcuts import render
from django.http import HttpResponse
from .services.downloader import Downloader
import json
import os
from django.conf import settings
from django.http import HttpResponse, Http404
from django.utils.encoding import smart_str


# Create your views here.
def video(request):
    if request.method == 'POST':
        req_body = dict(request.POST)
        downloader = Downloader()
        downloader.set_single_video_link(str(req_body['link']))
        res_body = dict()
        res_body["link"] = req_body["link"][0]
        res_body["title"] = downloader.get_title()
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
        res_body["title"] = downloader.get_title()
        res_body["available_links"] = [i.mime_type for i in downloader.get_available_audio_streams()]
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
        res_body["title"] = downloader.get_title(is_playlist=True)
        # res_body['thumbnail'] = downloader.get_video_thumbnail()
        return render(request, 'downloader/playlist.html', {'data': res_body})
    return render(request, 'downloader/playlist.html')

def other_projects(request):
    return render(request, 'downloader/other_projects.html')

def download_video(request):
    if request.method == 'GET':
        return render(request, '500.html', status=500)
    req_body = dict(request.POST)
    print("\n\nvideo downloaded \n\n")
    downloader = Downloader()
    downloader.set_single_video_link(str(req_body['link']))
    downloader.download_single_video(0)

    response = HttpResponse(content_type='application/force-download') # mimetype is replaced by content_type for django 1.7
    response['Content-Disposition'] = 'attachment; filename=%s' % (smart_str(downloader.get_title()) + ".mp4")

    response['X-Sendfile'] = smart_str('/media/' + downloader.get_title() + '.mp4')
    # It's usually a good idea to set the 'Content-Length' header too.
    # You can also set any other required headers: Cache-Control, etc.
    return response