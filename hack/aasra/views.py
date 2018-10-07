from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import requests
from .models import phone, Quote
# Create your views here.
def api(request):
	# These code snippets use an open-source library. http://unirest.io/python
	#response = requests.get("https://talaikis.com/api/quotes/")
	#user=response.json()
	#listofquotes=[]
	#while listofquotes==[]:
	#	for quote in user:
	#		if quote['cat'] in 'inspirational':
	#			listofquotes.append(quote['quote'])
	quoteslist=list(Quote.objects.all())
	numlist=list(phone.objects.all())
	return render(request,'aasra/index.html',{'qlist':quoteslist,'numlist':numlist})


def upvote(request,no):
	upvotedno=get_object_or_404(phone,phone_no = no)
	upvotedno.no_likes+=1
	upvotedno.save()
	print(str(upvotedno.phone_no)+"likes = "+str(upvotedno.no_likes))

	return HttpResponseRedirect("/")


