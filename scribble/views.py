from django.shortcuts import render, redirect, HttpResponse
from .models import Scribble

def index(request):
    if request.method == 'POST':
        Scribble.objects.create(
            scribble=request.POST['scribble'],
            tag=request.POST.get('tag') or 'Anonymous',  # se vuoto, mette Anonymous
        )
        return redirect('/scribble')

    scribbles = Scribble.objects.all()
    return render(request, 'index.html', {'scribbles': scribbles})

def detail(request, extra_input):
    # input_specifico contiene la parte finale dell'URL
    context = {'extra_input': extra_input}
    return HttpResponse(extra_input + " cane cane")#render(request, 'detail.html', context)