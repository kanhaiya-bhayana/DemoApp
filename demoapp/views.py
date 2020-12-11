from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    dict={'NAME':'Kanhaiya Bhayana','MAdeBy':'Sunshine Developers'}
    return render(request,'demoapp/index.html',dict)

def python(request):
    return render(request,'demoapp/python.html')

def about(request):
    return render(request, 'demoapp/about.html')

def remove_punc(request):
    return render(request, 'demoapp/remove_punc.html')


def result_rem_punc(request):

    global counter, params
    count = 0
    # getting the value from the url of the page result_rem_punc..
    string = request.POST.get('ipstring', 'default')
    rm_punc = request.POST.get('rm_punc', 'off')
    char_count = request.POST.get('char_count', 'off')
    analyzed = ""
    punctuatons = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
    if rm_punc == "on":
        for char in string:
            if char not in punctuatons:
                analyzed = analyzed + char
        params = {'ipstring': string, 'opstring': analyzed, 'msg': 'Success'}  # we are passing this dictionary as a parameter to the page restlt_rem_punc...
        return render(request, 'demoapp/result_rem_punc.html', params)
    elif char_count == "on":
        lenth_of_string = len(string) - string.count(" ") # - string.count(" ") i.e. minus the spaces count from the output...
        counter = {'ipstringchar':string, 'cnt':lenth_of_string, 'msg1':'Counted Sucessfully'}
        return render(request, 'demoapp/result_rem_punc.html', counter)

    else:
        return HttpResponse("Please select any operation!")






