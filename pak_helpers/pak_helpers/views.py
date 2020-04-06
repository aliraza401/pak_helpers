from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from helper.filters import HelperFilter
from django.contrib.auth.models import User
from helper.decorators import unacthenticated_user
from contact.models import Contact, Question
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from helper.models import Helper



def index(request):
    template = 'index.html'
    helpers = Helper.objects.order_by('rating')[:3]
    context = {'helpers': helpers, }

    return render(request, template, context)


def listView(request):
    template = 'list_view.html'
    helpers = Helper.objects.all()

    myFilter = HelperFilter(request.GET, queryset=helpers)
    helpers = myFilter.qs

    page = request.GET.get('page', 1)
    paginator = Paginator(helpers, 9)
    try:
        helpers = paginator.page(page)
    except PageNotAnInteger:
        helpers = paginator.page(1)
    except EmptyPage:
        helpers = paginator.page(paginator.num_pages)

    context = {
        'helpers':helpers,
        'myFilter': myFilter,
    }

    return render(request, template, context)


def detailView(request, id):
    template = 'detail_view.html'
    user = User.objects.get(id=id)
    helper = Helper.objects.get(user=user)
    category_list = helper.category.all()

    context = {
        'helper': helper,
        'category_list': category_list,
    }

    return render(request, template, context)


def loginView(request):
    template = 'login.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            group = user.groups.all()[0].name
            if group == 'helper':
                login(request, user)
                return redirect('helper:helper_dashboard')
            elif group == 'employer':
                login(request,user)
                return redirect('employer:dashboard_employer')
            else:
                messages.info(request, 'Invalid username or password \ncontact support')
        else:
            messages.info(request, 'Invalid username or password')

    context = {}
    return render(request, template, context)


def logoutView(request):
    logout(request)
    return redirect('/')

def contactView(request):
    template = 'contact_form.html'

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Contact.objects.create(name=name,email=email,message=message)
        return redirect('/')

    context = {

    }

    return render(request,template,context)


def helpView(request):
    template = 'help.html'
    questions = Question.objects.all()[:5]

    context = {
        'questions' : questions,
    }

    return render(request,template,context)


