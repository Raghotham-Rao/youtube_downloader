from django.shortcuts import render
from django.http import HttpResponse
from .services.downloader import Downloader
import json
import os
from django.conf import settings
from django.http import HttpResponse, Http404


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
    print(req_body)
    downloader = Downloader()
    downloader.set_single_video_link(str(req_body['link']))
    downloader.download_single_video(0)

    # file_path = os.path.join(settings.MEDIA_ROOT, path)
    # if os.path.exists(file_path):
    #     with open(file_path, 'rb') as fh:
    #         response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
    #         response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
    #         return responsefile_path = os.path.join(settings.MEDIA_ROOT, path)
    # if os.path.exists(file_path):
    #     with open(file_path, 'rb') as fh:
    #         response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
    #         response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
    #         return response
    return HttpResponse('Downloaded at the server')