from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
        #return HttpResponse('Hello')
        return render(request,'home.html')


def about(request):
        #return HttpResponse('Hello')
        return render(request,'about.html')

def count(request):
        fulltext = request.GET['fulltext']
        wordlist = fulltext.split()

        worddictionary = {}

        for x in wordlist:
            if x in worddictionary:
                worddictionary[x] += 1
            else:
                worddictionary[x] = 1

        sorted_worddictionary = sorted(worddictionary.items(), key=lambda x:x[1],  reverse =True)

        return render(request,'count.html',{'fulltext':fulltext, 'wordcount':len(wordlist), 'worddictionary':sorted_worddictionary})
