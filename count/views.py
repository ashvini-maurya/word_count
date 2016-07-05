from django.shortcuts import render
import string


def index(request):

    return render(request, 'count/index.html')


def getValue(request):
    if request.method == 'POST':
        my_file = request.FILES['filename'].read()
        line=len(my_file.splitlines())
        words=len(string.split(my_file))
        characters = len(my_file)

        # print len(my_file.splitlines()), len(string.split(my_file)), len(my_file)
        return render(request,'count/showdata.html',{'line':line,'words':words, 'characters': characters})