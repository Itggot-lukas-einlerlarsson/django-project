from django.shortcuts import render

def index(request):
    name = request.GET.get("name") or "world"
    return render(request, "base.html", {"name" : name})

def book_search(request):
    search_text = request.GET.get("search") or "world"
    return render(request, "book_search.html", {"search_text" : search_text})
