from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Word

def home(request):
    words = Word.objects
    return render(request, 'words/home.html', {'words':words})

@login_required(login_url="/accounts/signup")
def create(request):
    if request.method=='POST':
        if request.POST['word'] and  request.POST['meaning'] and request.POST['usedinsen']:
            wordon = Word()
            wordon.word = request.POST['word']
            wordon.meaning = request.POST['meaning']
            wordon.usedinsen = request.POST['usedinsen']
            wordon.maker = request.user
            wordon.save()
            return redirect('/words/'+str(wordon.id))


        else:
            return render(request,'words/create.html',{'error':' All fields are required' })


    else:
        return render(request,'words/create.html')

def detail(request, word_id):
    word = get_object_or_404(Word, pk=word_id)
    return render(request, 'words/detail.html',{'word':word})
