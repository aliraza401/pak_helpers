from django.shortcuts import render, redirect

from .forms import CreateUserForm, HelperForm, UpdateHelperForm, UpdateUserForm
from .models import User, Helper, Rewiew
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .decorators import allowed_user
from django.contrib import messages

# Create your views here.

 
def createHelplerView(request):
    template = 'helper/create_helper.html'
    form1 = CreateUserForm()
    form2 = HelperForm()

    if request.method == 'POST': 
        form1 = CreateUserForm(request.POST)
        form2 = HelperForm(request.POST, request.FILES)
        

        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            group = Group.objects.get(name='helper')
            user.groups.add(group)
            profile = form2.save(commit=False)
            profile.user = User.objects.get(username=user)
            profile.rating = 5
            profile.profile_visible = True
            profile.save()
            messages.success(request, 'Helper account created for '+ profile.user.username )
            return redirect('login')
        else:
            print(form1.errors)
            print(form2.errors)

    context = {
        "form1": form1,
        "form2": form2,
    }

    return render(request, template, context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['helper'])
def UpdateHelplerView(request):
    template = 'dash/update_helper.html'
    user = request.user.helper
    form2 = UpdateHelperForm(instance=user)

    if request.method == 'POST':
        form2 = UpdateHelperForm(request.POST,request.FILES,instance=user)
        if form2.is_valid():
            form2.save()
            return redirect('helper:helper_dashboard')
        else:
            print(form2.errors)

    context = {
        "form2": form2,
    }

    return render(request, template, context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['helper'])
def helperDashboardView(request):
    template = 'dash/helper_dashboard.html'
    context = {
 
    }

    return render(request, template, context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['helper'])
def helperReviewsView(request):
    template = 'dash/reviews.html'
    context = {

    }

    return render(request, template, context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['helper'])
def helperDeactivateView(request):
    template = 'dash/deactivate_account.html'

    if request.method == 'POST':
        request.user.is_active = False
        request.user.save()
        return redirect('/')

    context = {

    }

    return render(request, template, context)


def error_404_page(request,exception):
    template = '404_page.html'
    context = {

    }

    return render(request, template, context)





