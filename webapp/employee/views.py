from django.shortcuts import render,HttpResponse,redirect
from employee.forms import formExample,studentForm,teacherForm,sgpgForm
from employee.models import student,teacher,sgpg
from django.contrib.auth.decorators import login_required
# Create your views here.

def view(request, pk):
    data = student.objects.get(id=pk)
    return render(request, 'view.html', {'data': data})


def delete(request, pk):
    data=student.objects.get(id=pk)
    data.delete()
    return redirect('index')

def update(request, pk):
    # select * from student where id=pk
    data = student.objects.get(id=pk)
    form = studentForm(instance=data) #Attach data to formfield
    if request.method == "POST":
        form = studentForm(request.POST,instance=data)
        if form.is_valid():
            #form.save()
            stu=student()
            stu.id=pk
            stu.name=form.cleaned_data['email'].split('@')[0]
            stu.email=form.cleaned_data['email']
            stu.address=form.cleaned_data['address']
            stu.save()
            return redirect('index')
    return render(request, 'update.html', {'form': form})

#Create form

#@login_required(login_url='/signin')
def create(request):
    form = studentForm()
    if request.method == "POST":
        form = studentForm(request.POST)
        if form.is_valid():
            #form.save()
            stu=student()
            stu.name=form.cleaned_data['email'].split('@')[0]
            stu.email=form.cleaned_data['email']
            stu.address=form.cleaned_data['address']
            stu.save()
            return redirect('index')
    return render(request,'create.html',{'form':form})

#@login_required(login_url='/signin')
def index(request):
    #select * from student
    data=student.objects.all()
    return render(request,'index.html',{'data':data})

def helloDjango(request):
    l1={1,2,3,4}
    d1={'a':1,'b': 2,'c': 3}
    data={'l1':l1,'name':'xyz','phone':9895199006,'d1':d1}
    return render(request,'hello.html',data)
   #return HttpResponse('<h2>Hello</h2>')

def hellopython(request):
    return render(request, 'hello_python.html')


def nav1(request):
    return render(request, 'nav1.html')

def nav2(request):
    return render(request, 'nav2.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def formTest(request):
    form = formExample()
    if request.method=="POST":
        form=formExample(request.POST)
        if form.is_valid():
            pass

    return render(request, 'formTest.html',{'form': form})



#techer


def teacher_view(request, pk):
    data = teacher.objects.get(id=pk)
    return render(request, 'teach/view.html', {'data': data})


def teacher_delete(request, pk):
    data=teacher.objects.get(id=pk)
    data.delete()
    return redirect('teacherindex')

def teacher_update(request, pk):
    # select * from student where id=pk
    data = teacher.objects.get(id=pk)
    form = teacherForm(instance=data) #Attach data to formfield
    if request.method == "POST":
        form = teacherForm(request.POST,instance=data)
        if form.is_valid():
            #form.save()
            tch = teacher()
            tch.name = form.cleaned_data['name']
            tch.student = form.cleaned_data['student']
            tch.email = form.cleaned_data['email']
            tch.city = form.cleaned_data['city']
            tch.gender = form.cleaned_data['gender']
            tch.is_active = form.cleaned_data['is_active']
            tch.save()
            return redirect('teacherindex')
    return render(request, 'teach/update.html', {'form': form})

#Create form
def teacher_create(request):
    form = teacherForm()
    if request.method == "POST":
        form = teacherForm(request.POST)
        if form.is_valid():
            #form.save()
            tch=teacher()
            tch.name=form.cleaned_data['name']
            tch.student=form.cleaned_data['student']
            tch.email=form.cleaned_data['email']
            tch.city=form.cleaned_data['city']
            tch.gender=form.cleaned_data['gender']
            tch.is_active=form.cleaned_data['is_active']
            tch.save()
            return redirect('teacherindex')
    return render(request,'teach/create.html',{'form':form})

def teacher_index(request):
    #select * from student
    data=teacher.objects.all()
    return render(request,'teach/index.html',{'data':data})


def sgpg(request):
    form = sgpgForm()
    if request.method == "POST":
        form = sgpgForm(request.POST)
        if form.is_valid():
            insert=sgpg()
            insert.first_name=form.cleaned_data['first_name']
            insert.middle_name=form.cleaned_data['middle_name']
            insert.last_name=form.cleaned_data['last_name']
            insert.save()


            return redirect('sgpgindex')
    return render(request,'sgpg_insert.html',{'form':form})

def sgpg_index(request):
    #select * from student
    data=sgpg.objects.all()
    return render(request,'sgpg_index.html',{'data':data})
