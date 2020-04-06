from django.http import HttpResponse
from django.shortcuts import redirect


def unacthenticated_user(view_func):
    def wrapper_func(request , *args , **kwargs):
        if request.user.is_authenticated:
            return view_func(request , *args , **kwargs)            
        else:
            return redirect('helper:helper_reviews' , id = request.user.id)
           
    return wrapper_func


def allowed_user(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request , *args , **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group in allowed_roles:
                    return view_func(request , *args , **kwargs)
                else:
                    return HttpResponse("not permited")
            
        return wrapper_func
    return decorator 


