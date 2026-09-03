from django.shortcuts import redirect


# Authentciation
def auth(view_function):
    def wrapped(req,*args,**kwargs):
        if req.user.is_authenticated == False:
            return redirect("login")    
        return view_function(req,*args,**kwargs)
    return wrapped


def guest(view_function):
    def wrapped(req,*args,**kwargs):
        if req.user.is_authenticated:
            return redirect("dashboard")    
        return view_function(req,*args,**kwargs)
    return wrapped