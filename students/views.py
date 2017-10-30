from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Student


# Views for Students
def students_list(request):
    students = Student.objects.all()

    # try to order students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('last_name', 'first_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()

    # paginate students
    paginator = Paginator(students, 3)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver first page.
        students = paginator.page(1)
    except EmptyPage:
        # if pga is out of range (e.g. 9999), deliver
        # last page or result.
        students = paginator.page(paginator.num_pages)

    return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
    return HttpResponse('Student Add Form')

def students_edit(request, sid):
    return HttpResponse('Edit Student %s' % sid)

def students_delete(request, sid):
    return HttpResponse('Delete Student %s' % sid)

# Views for Groups
def groups_list(request):
    students = (
    {'id' : 1,
    'first_name': 'Vitaliy',
    'last_name': 'Pdoba',
    'ticket': 235,
    'image': 'img/me.jpeg'},
    {'id': 2,
    'first_name': 'Korost',
    'last_name': 'Andriy',
    'ticket': 2123,
    'image': 'img/piv.png'}
    )
    return render(request, 'students/groups_list.html', {'students': students})

def groups_add(request):
    return HttpResponse('Group Add Form')

def groups_edit(request, gid):
    return HttpResponse('Edit Group %s' % gid)

def groups_delete(request, gid):
    return HttpResponse('Delete Group %s' % gid)
