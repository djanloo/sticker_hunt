from django.shortcuts import render, redirect, HttpResponse
from .models import Scribble, ScribblePointInfo

def index(request):

    extra_input = request.session.get('extra_info', None)

    # recupera il token dal DB
    scribble_info = None

    if extra_input:
        try:
            scribble_info = ScribblePointInfo.objects.get(token=extra_input)
        except ScribblePointInfo.DoesNotExist:
            scribble_info = None

    if request.method == 'POST' and scribble_info is not None:
        Scribble.objects.create(
            scribble=request.POST['scribble'],
            tag=request.POST.get('tag') or 'Anonymous',
            scribble_point=scribble_info
        )
        return redirect('/scribble')
    print("Goo goo ga ga")
    scribbles = Scribble.objects.filter(
        scribble_point=scribble_info
    ).order_by('-created_at')
    return render(request, 'index.html', {'scribbles': scribbles, 'scribble_info':scribble_info})

def detail(request, extra_input):
    request.session['extra_info'] = extra_input
    return redirect('/scribble')