from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    if request.method == 'POST':
        price = request.POST.get('search_term')
        return HttpResponse(f"you seached for {price}")

    else:
        return render(request, 'deals/index.html')

def about(request):
    return render(request, 'deals/aboutus.html')
