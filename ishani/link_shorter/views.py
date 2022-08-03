from django.shortcuts import render
from django.http import HttpResponse
from link_shorter.models import ShortUrl
from random import choices

charForShort = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]

def main_page(request):
    return render(request,"index.html")
def shorter(request):
    url = request.GET["url"] 
    while True:
        s = "".join(choices(charForShort,k=6))
        try:
            ShortUrl.objects.get(shortUrl = s)
        except:
            if url[0:8] != "https://" and url[0:7] != "http://":
                url = "http://" + url
            su = ShortUrl(mainUrl=url,shortUrl=s)
            su.save()
            break

    
    return render(request,"short.html",{"url":str(request.get_host())+"/s/"+str(s)})
def showShort(request,s):
    try:
        url = ShortUrl.objects.get(shortUrl=s).mainUrl
    except:
        url = "1"
    return render(request,"show.html",{"url":url})
