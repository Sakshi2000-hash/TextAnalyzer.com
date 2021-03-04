#this file is created by me
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')
    removepunc=request.GET.get('removepunc','off')
    capital = request.GET.get('capital','off')
    low = request.GET.get('low','off')
    title_text = request.GET.get('title_text','off')
    word_count = request.GET.get('word_count','off')
    find = request.GET.get('find','off')
    count_of_your_word = request.GET.get('count_of_your_word','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        if capital == 'on':
        	analyzed = analyzed.upper()
        	params = {'purpose': 'Removed Punctuations And Uppercased', 'analyzed_text': analyzed}
        	# if word_count == 'on':
        	# 	count = 0;
        	# 	for char in djtext:
        	# 		if char == ' ':
        	# 			count = count+1
        	# 	st1 = 'the word count is '
        	# 	st2 = str(count)
        	# 	st3 = st1 + st2
        	# 	analyzed = analyzed + " " + st3
        	# 	params = {'purpose':'Removed Punctuations And Uppercased ','analyzed_text' : analyzed}

        	# 	# count = 0;
        	# 	# for char in djtext:
        	# 	# 	if char == ' ':
        	# 	# 		count = count+1
        	# 	# st1 = 'the word count is '
        	# 	# st2 = str(count)
        	# 	# st3 = st1+st2
        	# 	# analyzed = analyzed + " "+ st3
        	# 	# params = {'purpose': 'Removed Punctuations,Uppercased And Count of Word is ', 'analyzed_text': analyzed}
         #    params = {'purpose': 'Removed Punctuations And Uppercased', 'analyzed_text': analyzed}

        elif low == 'on':
        	analyzed = analyzed.lower()
        	params = {'purpose': 'Removed Punctuations And Lowercased', 'analyzed_text': analyzed}
        elif title_text == 'on':
        	analyzed = analyzed.capitalize()
        	params = {'purpose': 'Removed Punctuations And Titlecased', 'analyzed_text': analyzed}

        elif word_count == 'on':
        	count = 0;
        	for char in djtext:
        		if char == ' ':
        			count = count+ 1
        	st1 = "the word count is "
        	st2 = str(count)
        	st3 = st1+st2
        	analyzed = analyzed + " " + st3
        	params = {'purpose': 'Removed Punctuations and Word_Count', 'analyzed_text': analyzed}

        # elif word_count == 'on' and capital == 'on':
        # 	analyzed = analyzed.upper()
        # 	count = 0;
        # 	for char in djtext:
        # 		if char == ' ':
        # 			count = count+ 1
        # 	st1 = "the word count is "
        # 	st2 = str(count)
        # 	st3 = st1+st2
        # 	analyzed = analyzed + " " + st3
        # 	params = {'purpose': 'Removed Punctuations,Uppercased And Word_Count', 'analyzed_text': analyzed}



        else:
        	params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}





   
        return render(request, 'analyze.html', params)


    elif capital == 'on':
    	analyzed = djtext.upper()
    	params = {'purpose': 'Capital Text', 'analyzed_text': analyzed}
    	return render(request, 'analyze.html', params)



    elif low == 'on':
    	analyzed = djtext.lower()
    	params = {'purpose': 'Lower Text', 'analyzed_text': analyzed}
    	return render(request, 'analyze.html', params)

    elif title_text == 'on':
    	djtext.capitalize()
    	params = {'purpose': 'Title Text', 'analyzed_text': djtext}
    	return render(request, 'analyze.html', params)

    elif word_count == 'on':
    	count = 0
    	for char in djtext:
    		if char == ' ':
    			count = count+1
    	params = {'purpose':'Total Word Count in your text','analyzed_text':count+1}
    	return render(request,'analyze.html',params)

    



    else:
        return HttpResponse('Error')