from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect

# Create your views here.
colours = ["success","error","warning","info"]
from yi2one.models import finds_20
def red(req):
    return render(req,"CV1.html",{"CV1":finds_20,"colours":colours})
def canvas(req):
    return render(req,'canvas.html')
def makesure(req):
    return render(req, 'makesure.html')