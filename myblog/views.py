from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect
from myblog.models import myblog
from django.template.response import TemplateResponse as TR
def home(request):
	return render_to_response("flash.html",)

def hello(request):
	a=myblog.objects.all()
	d={'a':a}
	return TR(request,"index.html",d)
