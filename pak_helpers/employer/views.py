from django.shortcuts import render, redirect
from helper.forms import CreateUserForm
from .forms import EmployerForm,UpdateEmployerForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from helper.decorators import allowed_user
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here
def employerCreateView(request):
    template = 'employer/create_employer.html'
    form1 = CreateUserForm()
    form2 = EmployerForm()

    if request.method == 'POST':
        form1 = CreateUserForm(request.POST)
        form2 = EmployerForm(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            group = Group.objects.get(name='employer')
            user.objects.add(group)
            profile = form2.save(commit=False)
            profile.user = User.objects.get(username=user)
            messages.success(request, 'Employer account created for '+ request.user.username  )
            form2.save()
        else:
            print(form1.errors)
            print(form2.errors)

    context = {
        'form1': form1,
        'form2': form2,
    }

    return render(request, template, context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['employer'])
def employerUpdateView(request):
    template = 'emp_dash/update_employer.html'
    user = request.user.employer
    form2 = UpdateEmployerForm(instance=user)

    if request.method == 'POST':
        form2 = UpdateEmployerForm(request.POST,request.FILES,instance=user)
        if form2.is_valid():
            form2.save()
            return redirect('employer:dashboard_employer')
        else:
            print(form2.errors)

    context = {
        "form2": form2,
    }

    return render(request, template, context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['employer'])
def employerDashboardView(request):
    template = 'emp_dash/employer_dashboard.html'
    context = {

    }

    return render(request, template, context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['employer'])
def employerDeactivateView(request):
    template = 'emp_dash/deactivate_account.html'

    if request.method == 'POST':
        request.user.is_active = False
        request.user.save()
        return redirect('/')

    context = {

    }

    return render(request, template, context)