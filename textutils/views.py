from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newline = request.POST.get('nlremover','off')
    exspacerem = request.POST.get('exspacerem','off')
    if removepunc == "on":
        punctuations = '''!@#$%^&*()_+=`~[{]}'"\|><,/?'''
        analyze= ""
        for char in djtext:
            if char not in punctuations:
                analyze = analyze + char

        params = {'purpose': 'Remove Punctuations','analyzed_text': analyze}
        return render(request, 'analyze.html',params)
    elif(fullcaps == "on"):
        analyze = ""
        for char in djtext:
            analyze += char.upper()
        
        params = {'purpose': 'Changed to Upper Case','analyzed_text': analyze}
        return render(request, 'analyze.html',params)
    elif(newline == "on"):
        analyze = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyze += char
        
        params = {'purpose': 'Removed New Line','analyzed_text': analyze}
        return render(request, 'analyze.html',params)
    elif(exspacerem == "on"):
        analyze = ""
        for index, char in enumerate(djtext):
            if not(djtext[index]== " " and djtext[index+1]== " "):
                analyze += char
        
        params = {'purpose': 'Extra Space Removed','analyzed_text': analyze}
        return render(request, 'analyze.html',params)


    else:
        return HttpResponse("Error")