from django.shortcuts import render
from django.http.response import HttpResponse

todo_list = []
# Create your views here.
def main(request):
    #app_name/templates/까지는 적혀있는거다. 알아서 찾아감.
    # print(request.GET)
    # print(request.GET['work'])
    # print(request.GET.get('work'))
    
    
    work = request.GET.get('work')
    if work:
        todo_list.append(work)
    context = {
        'work': todo_list
    }
    return render(request, 'todos/main.html', context)


def create(request):
    return render(request, 'todos/create.html')