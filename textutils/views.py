# I have created this File - Mohit Thapliyal
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse('<a href="https://www.facebook.com"> facebook </a>')
    # params = {'name':'Mohit','place':'Mars'}
    # return render(request, 'index.html', params)
    return render(request, 'index.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    # Checi checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercounter = request.POST.get('charactercounter', 'off')

    # Check which checkbox is on
    purpose = ''
    if(removepunc == "on"):
        analyzed = ''
        punctuaions = '''!()-[]{};:'"\,<>//?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuaions:
                analyzed += char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        purpose = 'Removed Punctuations '

    if(fullcaps == 'on'):
        analyzed = djtext.upper()
        params = {'purpose': 'Changed to UPPERCASE', 'analyzed_text': analyzed}
        djtext = analyzed
        purpose += '| Changed to UPPERCASE '
        
    if(newlineremover == 'on'):
        analyzed = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed += char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed
        purpose += '| Removed New Lines '

    if(extraspaceremover == 'on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed += char
        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        djtext = analyzed
        purpose += '| Removed Extra Spaces '
            
    if(charactercounter == 'on'):
        analyzed = len(djtext)
        params = {'purpose': 'Characters Counted', 'analyzed_text': analyzed}
        purpose += '| Characters Counted'

    if removepunc == 'on' or fullcaps == 'on' or newlineremover == 'on' or extraspaceremover == 'on' or charactercounter == 'on':
        params = {'purpose': purpose, 'analyzed_text': analyzed}
        
    else:
        params = {'purpose': 'No Option Used', 'analyzed_text': djtext}
    
    # Analyse the text
    return render(request, 'analyze.html', params)