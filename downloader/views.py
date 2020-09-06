from django.shortcuts import render
from django.http import HttpResponse
from .services.downloader import Downloader
import json

# Create your views here.
def index(request):
    if request.method == 'POST':
        req_body = dict(request.POST)
        downloader = Downloader()
        downloader.set_single_video_link(str(req_body['link']))
        res_body = dict()
        res_body["link"] = req_body["link"][0]
        res_body["title"] = downloader.get_video_title()
        res_body["available_links"] = [(i.mime_type, i.resolution) for i in downloader.get_available_video_streams()]
        return render(request, 'downloader/index.html', {'data': res_body})
    return render(request, 'downloader/index.html')