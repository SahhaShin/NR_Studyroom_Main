from django.shortcuts import render, redirect, get_object_or_404
import datetime
from .models import Qa, Comment, Board

# Create your views here.

#산하
def main(request):
    return render(request,'main.html')

def preindex(request):
    return render(request,'Counter-Up-master/demo/preindex.html')


#성준재
def board(request):
    content = Board.objects
    return render(request, 'index.html', {'boards':content})

def create(request):
    return render(request, 'create.html')

def register(request):
    board = Board()
    board.name = request.GET['name']
    board.phone_number = request.GET['phone_number']
    board.start_date = request.GET['start_date']
    board.end_date = request.GET['end_date']
    board.start_time = request.GET['start_time']
    board.end_time = request.GET['end_time']
    board.people = request.GET['people']
    board.memo = request.GET['memo']
    date = request.GET['start_date'].split("-")
    board.m_d = str(date[1]+"_"+date[2])
    board.save()
    return redirect('cal')

def read(request):
    content = Board.objects
    # read = get_object_or_404(Board, pk=board_id)
    return render(request, 'read.html', {'boards':content})

def delete(request, board_id):
    delete = get_object_or_404(Board, pk=board_id)
    delete.delete()
    return redirect('cal')

# views파일에서 pk는 board_id로 고정
def update(request, board_id):
    change = get_object_or_404(Board, pk=board_id) 
    return render(request, 'update.html', {'change':change})

def update_board(request, board_id):
    up = get_object_or_404(Board, pk=board_id)
    up.name = request.GET['name']
    up.phone_number = request.GET['phone_number']
    up.start_date = request.GET['start_date']
    up.end_date = request.GET['end_date']
    up.start_time = request.GET['start_time']
    up.end_time = request.GET['end_time']
    up.people = request.GET['people']
    up.memo = request.GET['memo']
    up.save()
    return redirect('read') 


#재이
def post_index(request):
    qa = Qa.objects
    return render(request, 'post_index.html', {'qas':qa})

def post_create(request):
    return render(request, 'post_create.html')
    
def post_new(request):
    qa = Qa()
    qa.title = request.GET['title']
    qa.name = request.GET['name']
    qa.password = request.GET['password']
    qa.body = request.GET['body']
    if(request.GET.get('category') == '예약문의'):
        qa.category = '예약문의'
    elif(request.GET.get('category') == '기타문의'):
        qa.category = '기타문의'
    qa.save()
    return redirect('post_index')


def post_detail(request, qa_id):
    qa = get_object_or_404(Qa, pk=qa_id)
    comment = Comment.objects
    qaall = Qa.objects
    return render(request, 'post_detail.html', {'qa':qa,'comments':comment})

def post_update(request, qa_id):
    qa = get_object_or_404(Qa, pk=qa_id)
    return render(request, 'post_update.html', {'qa':qa})

def post_updat(request, qa_id):
    qa = get_object_or_404(Qa, pk=qa_id)
    qa.title = request.GET['title']
    qa.body = request.GET['body']
    qa.name = request.GET['name']
    qa.password = request.GET['password']
    qa.date = datetime.datetime.now()
    if(request.GET.get('category') == '예약문의'):
        qa.category = '예약문의'
    elif(request.GET.get('category') == '기타문의'):
        qa.category = '기타문의'
    qa.save()
    return redirect('/post_detail/'+str(qa_id))

def post_delete(request, qa_id):
    qa = get_object_or_404(Qa, pk=qa_id)
    qa.delete()
    return redirect('post_index')

def ccreate(request):
    if request.method == 'POST':
        comment=Comment()

        comment.cname = request.POST['cname']
        comment.content = request.POST['content']
        comment.post = Qa.objects.get(pk=request.POST['post'])

        comment.save()

        return redirect('post_detail/' + str(comment.post.id))
    return render(request, 'post_detail.html')

def cdelete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    post = get_object_or_404(Qa, pk=comment.post.id)
    comment.delete()
    return redirect('post_index')