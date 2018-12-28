from django.shortcuts import render,redirect
from myapp.models import Doubans,Biancheng,Keji
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from .forms import Custom_Table,Custom_Table2,Custom_Table3
from .models import Ordinarymember
# Create your views here.
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
def start(request):

  return render(request,'myapp/start.html',{"title":"爬虫图书搜索系统"})

def base(request):

  return render(request,'myapp/base.html')


def home(request):

  return render(request,'myapp/home.html',{"title":"爬虫图书搜索系统"})


def tuijian(request,index=1):
  list = Doubans.objects.all()

  paginator = Paginator(list, 6)
  # 得到当前的页面数据
  page = paginator.page(index)

  # 获取当前页面数，这里是传过来的index
  currentPage = int(index)

  # 下面这段逻辑是保证标签始终是10个，所选的标签在中间
  if currentPage < 5:
    pageRange = range(1, 11)
  elif currentPage > paginator.num_pages - 6:
    pageRange = range(paginator.num_pages - 8, paginator.num_pages + 2)
  else:
    pageRange = range(currentPage - 4, currentPage + 6)
  # 将数据封装传到模板中
  context = {'page': page, 'pageRange': pageRange,'title':'通信书类',}

  return render(request,'myapp/tuijian.html',context)

def mine(request,index=1):

  list = Keji.objects.all()

  paginator = Paginator(list, 6)
  # 得到当前的页面数据
  page = paginator.page(index)

  # 获取当前页面数，这里是传过来的index
  currentPage = int(index)

  # 下面这段逻辑是保证标签始终是10个，所选的标签在中间
  if currentPage < 5:
    pageRange = range(1, 11)
  elif currentPage > paginator.num_pages - 6:
    pageRange = range(paginator.num_pages - 8, paginator.num_pages + 2)
  else:
    pageRange = range(currentPage - 4, currentPage + 6)
  # 将数据封装传到模板中
  context = {'page': page, 'pageRange': pageRange,'title':'科技书类',}
  return render(request,'myapp/mine.html',context)


def lianxi(request):

  return render(request,'myapp/lianxi.html',{"title":"联系我们"})

def like(request,index=1):
  list = Biancheng.objects.all()

  paginator = Paginator(list, 6)
  # 得到当前的页面数据
  page = paginator.page(index)

  # 获取当前页面数，这里是传过来的index
  currentPage = int(index)

  # 下面这段逻辑是保证标签始终是10个，所选的标签在中间
  if currentPage < 5:
    pageRange = range(1, 11)
  elif currentPage > paginator.num_pages - 6:
    pageRange = range(paginator.num_pages - 8, paginator.num_pages + 2)
  else:
    pageRange = range(currentPage - 4, currentPage + 6)
  # 将数据封装传到模板中
  context = {'page': page, 'pageRange': pageRange,'title':'编程书类',}

  return render(request,'myapp/like.html',context)

def login1(request):
  if request.method == 'POST':
      login_table = Custom_Table3(data = request.POST)
      if login_table.is_valid():
        user = authenticate(request,username= login_table.cleaned_data['username'],password=login_table.cleaned_data['password'])
        login(request, user)
        return redirect('myapp:home')

  else:
     login_table = Custom_Table3()
     content = {'login_table':login_table, 'user': request.user}

     return render(request, 'myapp/login.html', content)


def loginout(request):
       logout(request)
       return redirect('myapp:home')

def register(request):
  if  request.method == 'POST':
      registerform = Custom_Table(request.POST)
      if registerform.is_valid():
          registerform.save()
          user = authenticate(username=registerform.cleaned_data['username'], password=registerform.cleaned_data['password1'])
          user.email = registerform.cleaned_data['email']
          Ordinarymember(用户=user,昵称=registerform.cleaned_data['昵称'],生日=registerform.cleaned_data['生日']).save()
          login(request, user)
          return redirect('myapp:home')
  else:

    registerform = Custom_Table()
  content = {'registerform':registerform,"title":"注册"}
  return render(request,'myapp/register.html',content)


@login_required(login_url='myapp:login')
def user_center(request):
    content = { 'user':request.user}
    return render(request,'myapp/user_center.html',content)

@login_required(login_url='myapp:login')
def edit_profile(request):
    if request.method == 'POST':
        Edit_Form = Custom_Table2(request.POST,instance=request.user)
        if Edit_Form.is_valid():
            Edit_Form.save()
            request.user.ordinarymember.昵称 = Edit_Form.cleaned_data['昵称']
            request.user.ordinarymember.生日= Edit_Form.cleaned_data['生日']
            request.user.ordinarymember.save()
             #Ordinarymember(用户=user, 昵称=registerform.cleaned_data['昵称'], 生日=registerform.cleaned_data['生日']).save()

            return redirect('myapp:home')
    else:

        Edit_Form = Custom_Table2(instance=request.user)
    content = {'Edit_Form': Edit_Form,'user':request.user}

    return render(request,'myapp/edit_profile.html',content)
@login_required(login_url='myapp:login')
def change_password(request):

    if request.method == 'POST':
        Secret_Form = PasswordChangeForm(data=request.POST,user=request.user)
        if Secret_Form.is_valid():
            Secret_Form.save()
            return redirect('myapp:login')

    else:

        Secret_Form = PasswordChangeForm(user=request.user)
    content = {'Secret_Form': Secret_Form,'user':request.user}

    return render(request,'myapp/change_password.html',content)
