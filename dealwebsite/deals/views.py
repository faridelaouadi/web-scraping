from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'deals/index.html')

def results(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                return redirect('/')

    form = AuthenticationForm()
    return render(request = request,
                    template_name = "orders/login.html",
                    context={"form":form})
