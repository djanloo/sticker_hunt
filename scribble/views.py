from django.shortcuts import render, redirect
from .models import Scribble

def index(request):
    if request.method == 'POST':
        Scribble.objects.create(
            scribble=request.POST['scribble'],
            tag=request.POST.get('tag', 'Anonymous'),
        )
        return redirect('/scribble')

    scribbles = Scribble.objects.all()
    return render(request, 'index.html', {'scribbles': scribbles})