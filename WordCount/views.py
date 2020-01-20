from django.shortcuts import render
from django.http import HttpResponse
import operator
def homepage(request):
	return render(request ,'home.html')
def count(request):
	fulltext = request.GET['text']
	print(fulltext)
	number = fulltext.split()

	worddict = {}

	for word in  number:
		if word in worddict:
			worddict[word] += 1
		else:
			worddict[word] = 1
	sortedwords = sorted(worddict.items(), key = operator.itemgetter(1), reverse = True)
	return render(request,'count.html', {'fulltext': fulltext , 'COUNT': len(number), 'sortedwords': sortedwords})

def about(request):
		return render(request, 'about.html')
