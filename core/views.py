from django.shortcuts import render , redirect
from django.http import HttpResponse,HttpRequest
from requests import get
# Create your views here.
def download_file(url,name):

    # NOTE the stream=True parameter below
    with get(url, stream=True) as r:
        r.raise_for_status()
        with open(f"{name}.mp4", 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk:
                f.write(chunk)
    return url
def index(request):

    if request.method == "GET":
        return render(request,'index.html')
    elif request.method == "POST":
        l = []
        url = request.POST.get('urlVar')
        get_data = get(f'https://api.snappea.com/v1/video/details?url={url}', stream=True).json()
        #name = get_data['videoInfo']['title']
        video = get_data['videoInfo']['downloadInfoList'][6]['partList'][0]['urlList'][0]

        #download_file(video, name)
        l.append(video)
        link = {"urls": l}
        return render(request, 'index.html',link)
    #template_name = 'index.html'
    #return HttpResponse(template_name)



