from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateBoard
from .models import Board
# Create your views here.
def index(request):
    return render(request, 'index.html')

def boardMain(request):
    boards = Board.objects.all()

    return render(request, 'boardMain.html', {'boards': boards})

def createBoard(request):
    if request.method == 'POST':
        form = CreateBoard(request.POST)

        if form.is_valid():
            form.save()
            return redirect('boardMain')
        else:
            return redirect('index')
    else:
        form = CreateBoard()
        return render(request, 'createBoard.html', {'form': form})


def detail(request, board_id):
    board_detail = get_object_or_404(Board, pk=board_id)
    return render(request, 'detail.html', {'board_detail': board_detail})
