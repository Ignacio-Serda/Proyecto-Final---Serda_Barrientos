from django.shortcuts import render
from django.contrib.auth import login, authenticate
from app2.forms import *
from django.contrib.auth.decorators import login_required
from app2.models import *
from django.contrib.auth.models import User
from app1.models import *


def register_account(request):
    
    if request.method=="POST":
        
        form=UserRegisterForm(data=request.POST)
        
        if form.is_valid():
            
            form.save()
            
            user=form.save()
            
            login(request, user)
            
            blogs=Blog.objects.all()
            
            contexto2 = {
                "blogs":blogs[::-1]
            }
            
            return render(request, "index.html", context=contexto2)
        
        else:
            
            p1=str(form.cleaned_data['password1'])
            p2=str(form.cleaned_data['password1'])
            name=str(form.cleaned_data['first_name'])
            apellido=str(form.cleaned_data['last_name'])

            print(p1.isalnum())
            print(" " not in p1)
            if len(p1)<8:
                message="La contraseña debe contener más de 8 dígitos."
            elif p1.isalnum()==True or " " not in p1 == True:
                message="La contraseña debe ser alfanumérica y debe contener espacios"
            elif p1!=p2:
                message="La contraseña no concuerda con la confirmación."
            elif name.lower() in p1.lower() or apellido.lower() in p1.lower():
                message="La contraseña no debe estar relacionada con sus datos personales."
            else:
                message="El usuario ya existe."
            
            contexto = {
                "form":UserRegisterForm(),
                "bool":True,
                "message":message,
            }

            return render(request, "app2/register.html", context=contexto)
        
    
    contexto = {
        "form":UserRegisterForm()
    }
    
    return render(request, "app2/register.html", context=contexto)

def login_account(request):
    
    if request.method == "POST":
        
        form = Form_Login(data = request.POST)
        
        if form.is_valid():
            
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password1')

            user=authenticate(username=usuario, password=contra)
            
            if user is not None:
                
                login(request, user)
                blogs=Blog.objects.all()
            
                contexto2 = {
                    "blogs":blogs[::-1]
                }
            
                return render(request, "index.html", context=contexto2)
            
            else:
                
                contexto = {
                    "form":Form_Login(),
                    "bool":True,
                    "message":"Datos Incorrectos. Intente Nuevamente."
                }
        
                return render(request, "app2/login.html", context=contexto)
            
    
    contexto = {
        "form":Form_Login(),
        "bool":False,
        "message":""
    }
    
    return render(request, "app2/login.html", context=contexto)



def succesful_login(request):
    
    return render(request, 'app2/succesful-login.html')

@login_required

def profile(request):
    
    user = request.user
    
    if request.method=="POST":
        
        form=Form_Edit_1(request.POST, request.FILES)
        
        if form.is_valid():
            
            info=form.cleaned_data
            
            user.username=info["username"]
            user.first_name=info["first_name"]
            user.last_name=info["last_name"]
            user.email=info["email"]
            
            if list(Bio_Url.objects.filter(user_id=user.id).values())!=[]:
                bios_url=Bio_Url.objects.get(user_id=user.id)
                bios_url.bio=info["bio"]
                bios_url.url=info["url"]
                bios_url.save()
            else:
                bios_url=Bio_Url(user=request.user, bio=info["bio"], url=info["url"])
                bios_url.save()
            
            if info["imagen"]!=None:
                if list(Avatar.objects.filter(user_id=user.id).values())!=[]:
                    avatar=Avatar.objects.get(user_id=user.id)
                    avatar.imagen=info["imagen"]
                    avatar.save()
                else:
                    avatar=Avatar(user=user, imagen=info["imagen"])
                    avatar.save()
            try:
                user.save()
            except:
                data=list(Bio_Url.objects.filter(user_id=user.id).values())
    
                if data!=[]:
                    form=Form_Edit_1(initial={'first_name': user.first_name, "last_name":user.last_name, 'username' : user.username, "email": user.email, "bio": data[0]["bio"], "url": data[0]["url"]})
                else:
                    form=Form_Edit_1(initial={'first_name': user.first_name, "last_name":user.last_name, 'username' : user.username, "email": user.email})
                
                contexto={
                    "form": form,
                    "user": user,
                    "message": "El usuario ya existe"
                }
        
                return render(request, 'app2/profile.html', context=contexto)
            
            info=Blog.objects.all()

            contexto2={
                "blogs": info[::-1],
            }    
    
            return render(request, "index.html", context=contexto2)
            
            
        
    data=list(Bio_Url.objects.filter(user_id=user.id).values())
    
    if data!=[]:
        form=Form_Edit_1(initial={'first_name': user.first_name, "last_name":user.last_name, 'username' : user.username, "email": user.email, "bio": data[0]["bio"], "url": data[0]["url"]})
    else:
        form=Form_Edit_1(initial={'first_name': user.first_name, "last_name":user.last_name, 'username' : user.username, "email": user.email})
    
    contexto={
        "form": form,
        "user": user,
    }
    
    return render(request, 'app2/profile.html', context=contexto)



@login_required

def profile2(request):
    
    user = request.user
    
    if request.method=="POST":
        
        form=Form_Edit_2(request.POST)
        
        if form.is_valid():
            
            info=form.cleaned_data
            
            validacion=authenticate(username=user.username, password=info["password_actual"])
            
            
            if validacion is not None:
                
                if info["password1"]!="":
                    user = User.objects.get(username=request.user)
                    user.set_password(info["password1"])
                    user.save()
                    user2=authenticate(username=request.user, password=info["password1"])
            
                    if user2 is not None:
                        login(request, user2)
                        user.save()
                
                
                info=Blog.objects.all()

                contexto2={
                    "blogs": info[::-1],
                }    
        
                return render(request, "index.html", context=contexto2)
            
            else: 
                
                if info["password1"]!=info["password2"]:
                    message = "Las nuevas Contraseñas no coinciden"
                else:
                    message = "Contraseña Incorrecta. Intente Nuevamente."
                
                data=Bio_Url.objects.filter(user_id=user.id).values()
                
                form=Form_Edit_2(initial={'first_name': user.first_name, "last_name":user.last_name, 'username' : user.username, "email": user.email, "bio": data[0]["bio"], "url": data[0]["url"]})

                    
                contexto = {
                    "form": form,
                    "user": user,
                    "bool":True,
                    "message": message
                }

                return render(request, "app2/profile2.html", context=contexto)
    
    data=Bio_Url.objects.filter(user_id=user.id).values()
    
    form=Form_Edit_2(initial={'username' : user.username})
    
    contexto={
        "form": form,
        "user": user,
    }
    
    return render(request, 'app2/profile2.html', context=contexto)