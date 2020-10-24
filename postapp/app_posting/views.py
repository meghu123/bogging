from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import MycreationForm, posting,commentform
from .models import Post,comment,Tags
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User

# Create your views here.


def registerview(request):
    if request.method == 'GET':
        form = MycreationForm()
    else:
        form = MycreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Register")
    template_name = "app_posting/register.html"
    context = {'form': form}
    return render(request, template_name, context)



@login_required(login_url='login')
def commentView(request,pk):
    obj = Post.objects.get(pk=pk)
    comments = obj.comment_set.all()
    if request.method == 'GET':
        f1=commentform()
    else:
        print(request.POST)

        f1=commentform(request.POST)
        if f1.is_valid():
            f1.save()
            user=request.user
            data=Post.objects.filter(Create_by__username=user.username)
            return render(request,"app_posting/index.html",{'comments':comments,'data':data,})
    template_name = "app_posting/comments.html"
    context={'f1':f1,'comments':comments,'obj':obj}
    return render(request, template_name, context)






def postview(request):
    if request.method == 'GET':
        f1=posting()
    else:
        f1=posting(request.POST)
        if f1.is_valid():
            tag=f1.cleaned_data['tags']
            title=f1.cleaned_data['title']
            description=f1.cleaned_data['description']
            user=request.user
            p=Post(title=title,description=description,Create_by=user)
            p.save()
            tags=tag.split()
            for tg in tags:
                tg=tg.lower()
                t,tc=Tags.objects.get_or_create(tag_name=tg)
                p.tags.add(t or tc)
                p.save()
            return HttpResponse("post")
        return render(request,"app_posting/index.html",{'f1':f1})
    template_name = "app_posting/allpost.html"
    context={'f1':f1}
    return render(request, template_name, context)







def homeview(request):
    if request.method=='GET':
        obj = Post.objects.all()
        print(obj)
        f1=commentform()
        template_name="app_posting/home.html"
        context = {'stud': obj,'f1':f1}
        return render(request,template_name,context)
    else:
        find=request.POST.get('find')
        print(find)
        template_name="app_posting/search.html"
        context={'find':find}
        resp=render(request,template_name,context)
        request.session['find']=find
        # resp.set_cookie('find',find)
        return redirect("search")







def loginview(request):
    if request.method == 'GET':
        template_name = "app_posting/login.html"
        context = {}
        return render(request, template_name, context)
    else:
        u = request.POST['uname']
        p = request.POST['pass']
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)

            data=Post.objects.filter(Create_by__username=u)
            context={'data':data}
            return render(request,"app_posting/index.html",context)
        else:
            return HttpResponse("Invalid ........!!")





def logoutview(request):
    logout(request)
    return redirect("login")




def searchview(request):
    find=request.session['find']
    print(find)
    try:
        status = Post.objects.filter(Q(tags__tag_name__contains=find) |Q(tags__tag_name__icontains=find))
        print(status)
        return render(request, "app_posting/search.html", {"status": status})
    except:
        context = {'data': 'Not found'}
        return render(request, "app_posting/search.html", context)


def deleteview(request,pk):
    try:
        print(pk)
        data=Post.objects.get(pk=pk)
        print(data)
        if request.method=='GET':
            context={'obj':data}
            print("1")
            return render(request,"app_posting/delete.html",context)
        else:
            data.delete()
            return redirect('profile')
    except:
        return HttpResponse("Please enter correct value")




def updateview(request,pk):
    # try:
    #     data = Post.objects.get(pk=pk)
    #
    #     if request.method=='GET':
    #         form=posting(instance=data)
    #         template_name="app_posting/update.html"
    #         context={'form':form}
    #         return render(request,template_name,context)
    #     else:
    #         form=posting(request.POST,instance=data)
    #         if form.is_valid():
    #             data.save()
    #             return redirect('profile')
    #         context={'form':form}
    #         return render(request,"app_posting/update.html",context)
    # except:
    #     return HttpResponse("please enter valid input")
    #
    # try:
        print(pk)
        data = Post.objects.get(pk=pk)

        if request.method=='GET':
            user=request.user
            form=posting(initial={'title':data.title,'description':data.description,'Create_by':user})
            template_name="app_posting/update.html"
            context={'form':form}
            return render(request,template_name,context)
        else:
            form=posting(request.POST)
            if form.is_valid():
                data.title = form.cleaned_data.get('title')
                data.description = form.cleaned_data.get('description')
                data.save()
                return redirect('profile')
            context={'form':form}
            return render(request,"app_posting/update.html",context)
    # except:
    #     return HttpResponse("please enter valid input")





def Profileview(request):
    template_name="app_posting/index.html"
    user=request.user
    data = Post.objects.filter(Create_by__username=user.username)
    context = {'data': data}
    return render(request,template_name,context)


