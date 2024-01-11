from django.http import HttpResponseRedirect

from django.shortcuts import render

from random import randint

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def filename(request, filename):

    name = filename

    data2 = util.list_entries()

    lis = []

    for i in data2:

        if name == i:

            lis.append(i)

    if lis != []:

        data = util.get_entry(lis[0])

        return render(request, "encyclopedia/filename.html", {
            "title" : name , "datum" : data, "url" : request.path
        })
    
    elif lis == []:

        return render(request, "encyclopedia/404.html")
    
def form(request):
        
    if request.method == "POST":

        data = request.POST

        data = data.dict()

        data1 = data["q"]

        data2 = util.list_entries()

        lis = []

        for i in data2:

            if data1 in i:

                lis.append(i)

        if lis != []:

            return render(request, "encyclopedia/result.html", {
                "datum" : lis
            })
        
        else:

            return render(request, "encyclopedia/apology.html")
        
def create(request):

    if request.method == "GET":

        return render(request, "encyclopedia/create.html")
    
    elif request.method == "POST":

        data = request.POST

        data = data.dict()

        title = data["text"]

        content = data["content"]

        data2 = util.list_entries()

        lis = []

        for i in data2:

            if title == i:

                lis.append(i)

        if lis == []:

            util.save_entry(title, content)

            return HttpResponseRedirect(f'wiki/{title}')
        
        elif lis != []:

            return render(request, "encyclopedia/exists.html")
        
def edit(request, filename):

    name = filename

    if request.method == "GET":

        data = util.get_entry(name)

        return render(request, "encyclopedia/edit.html", {
            "url" : request.path , "datum" : data
        })
    
    elif request.method == "POST":

        data = request.POST

        data = data.dict()

        content = data["content"]

        util.save_entry(name, content)

        url = f"/wiki/{name}"

        return HttpResponseRedirect(url)
    
def random(request):

    num = 0

    lis = []

    data = util.list_entries()

    for i in data:

        num += 1

        lis.append(i)

    num -= 1

    random_number = randint(0 , num)

    data2 = lis[random_number]

    data3 = util.get_entry(data2)

    return render(request, "encyclopedia/filename.html", {
            "title" : data2 , "datum" : data3, "url" : request.path
        })