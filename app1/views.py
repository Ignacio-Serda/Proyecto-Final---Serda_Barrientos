from django.shortcuts import render
from app1.forms import *
from app1.models import *
from django.contrib import messages
from django.contrib.auth.models import User
from app2.models import *
from app2.forms import *

def home(request):
    
    info=Blog.objects.all()
    
    contexto={
        "blogs": info[::-1],
    }    
    return render(request, "index.html", context=contexto)

def creation_blog(request):
    
    if request.method=="POST":
        
        mi_formulario=Form_Blog(request.POST, request.FILES)
        
        if mi_formulario.is_valid():
            
            info=mi_formulario.cleaned_data
            
            data_save=Blog(
                titulo=info["titulo"],
                subtitulo=info["subtitulo"],
                cuerpo=info["cuerpo"],
                autor=info["autor"],
                imagen=info["imagen"]
            )
            
            data_save.save()
            
            info=Blog.objects.all()
    
            contexto2={
                "blogs": info[::-1],
            }    
    
            return render(request, "index.html", context=contexto2)
        
    nombre = request.user.first_name + " " + request.user.last_name
    
    contexto={
        "form": Form_Blog(initial={"autor":nombre}),
    }
    
    return render(request, "app1/create-blog.html", context=contexto)


def show_blogs(request):
    
    info=Blog.objects.all()
    
    user = request.user
    
    nombre= user.first_name + " " + user.last_name
    
    contexto={
        "blogs": info,
        "nombre_completo": nombre,
    }    
        
    return render(request, "app1/blogs.html", context=contexto)

def eliminar(request, id):
    
    user = request.user
    
    nombre= user.first_name + " " + user.last_name
    
    blog = Blog.objects.get(id=id)
    
    blog.delete()
    
    info = Blog.objects.all()
    
    contexto={
        "blogs": info,
        "nombre_completo": nombre,
    }    
    
    return render(request, "app1/blogs.html", context=contexto)
    

def edit_panel(request):
    
    users=User.objects.all()
    
    blogs=Blog.objects.all()
    
    contexto = {
        'blogs': blogs,
        'users': users[1::],
    }
    
    return render(request, 'app2/edit-panel.html', context=contexto)

def editar_user(request, id):
    
    user = User.objects.get(id=id)
    
    if request.method=="POST":
        
        form=Form_Edit_1(request.POST, request.FILES)
        
        if form.is_valid():
            
            info=form.cleaned_data
            
            user.username=info["username"]
            user.first_name=info["first_name"]
            user.last_name=info["last_name"]
            user.email=info["email"]
            
            if list(Bio_Url.objects.filter(user_id=id).values()) != []:
                bios_url=Bio_Url.objects.get(user_id=id)
                bios_url.bio=info["bio"]
                bios_url.url=info["url"]
                bios_url.save()
            else:
                bios_url=Bio_Url(user_id=id, bio=info["bio"], url=info["url"])
                bios_url.save()
            
            if info["imagen"]!=None:
                if list(Avatar.objects.filter(user_id=id).values()) != []:
                    avatar=Avatar.objects.get(user_id=id)
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
                "id": id,
            }    
    
            return render(request, "index.html", context=contexto2)
        
    data=list(Bio_Url.objects.filter(user_id=id).values())
    if data!=[]:
        form=Form_Edit_1(initial={'first_name': user.first_name, "last_name":user.last_name, 'username' : user.username, "email": user.email, "bio": data[0]["bio"], "url": data[0]["url"]})
    else:
        form=Form_Edit_1(initial={'first_name': user.first_name, "last_name":user.last_name, 'username' : user.username, "email": user.email})
    
    contexto={
        "form": form,
        "user": request.user,
        "id": id,
    }
    
    return render(request, 'app2/editar-users.html', context=contexto)

def editar_user2(request, id):
    
    user = User.objects.get(id=id)
    
    if request.method=="POST":
        
        form=Form_Edit_2_1(request.POST)
        
        if form.is_valid():
            
            info=form.cleaned_data
                
            if info["password1"]!="":
                
                user = User.objects.get(username=user.username)
                user.set_password(info["password1"])
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
                
                form=Form_Edit_2_1()

                    
                contexto = {
                    "form": form,
                    "user": user,
                    "bool": True,
                    "message": message
                }

                return render(request, "app2/profile2.html", context=contexto)
    
    form=Form_Edit_2_1()
    
    contexto={
        "form": form,
        "user": request.user,
    }
    
    return render(request, 'app2/profile2.html', context=contexto)

def leer_mas(request, id):
    
    if request.method=="POST":
    
        form=Form_Comentario(request.POST)
    
        if form.is_valid():
        
            info=form.cleaned_data
        
            comentario=Comentario(blog_id=id, contenido=info["contenido"], nombre=info["nombre"])
            comentario.save()
            
    blog = Blog.objects.get(id=id)
    
    comentarios=Comentario.objects.filter(blog_id=id)
    
    form = Form_Comentario(initial={"nombre":request.user.first_name})

    
    contexto = {
        "blog":blog,
        "form":form,
        "user":request.user,
        "comentarios":comentarios[::-1]
    }
    
    return render(request, "app1/leer-mas.html", context=contexto)
    
def about_me(request):
    
    return render(request, "app1/about-me.html")

def eliminar_blogs(request, id):
    
    blog=Blog.objects.get(id=id)
    
    blog.delete()
    
    users=User.objects.all()
    
    blogs=Blog.objects.all()
    
    contexto = {
        'blogs': blogs,
        'users': users[1::],
    }
    
    return render(request, 'app2/edit-panel.html', context=contexto)

def eliminar_users(request, id):
    
    user=User.objects.get(id=id)
    
    user.delete()
    
    users=User.objects.all()
    
    blogs=Blog.objects.all()
    
    contexto = {
        'blogs': blogs,
        'users': users[1::],
    }
    
    return render(request, 'app2/edit-panel.html', context=contexto)

def about_me(request):
    
    return render(request, 'app1/about-me.html')


def edit_blogs(request, id):
    
    nombre=request.user
    
    blog=Blog.objects.get(id=id)
    
    if request.method=="POST":
        
        form=Edit_Form_Blog(request.POST)
        
        if form.is_valid():
            
            info=form.cleaned_data
    
            blog.titulo = info["titulo"]
            blog.subtitulo = info["subtitulo"]
            blog.cuerpo = info["cuerpo"]
            
            blog.save()
            
            info = Blog.objects.all()
            
            nombre = request.user.first_name + " " + request.user.last_name
            
            contexto={
                "blogs": info,
                "nombre_completo": nombre,
            }    
        
            return render(request, "app1/blogs.html", context=contexto)
    
    info = Blog.objects.all()
    
    data_blog=Blog.objects.get(id=id)
    
    nombre = request.user.first_name + " " + request.user.last_name
    
    contexto={
        "blogs": info,
        "nombre_completo": nombre,
        "form": Edit_Form_Blog(initial={'titulo': data_blog.titulo, 'subtitulo': data_blog.subtitulo, 'cuerpo': data_blog.cuerpo})
    }    
    
    return render(request, "app1/edit-blog.html", context=contexto)