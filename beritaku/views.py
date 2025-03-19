from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .forms import *
from django.shortcuts import get_object_or_404
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate, login
from django.core.files.storage import FileSystemStorage  

# Create your views here.
def index(request):

    template = loader.get_template('home.html')
    context = {
        'title' : 'beritaku.id',
    }
    return HttpResponse(template.render(context, request))

def home(request) :

    template = loader.get_template('home.html')
    context = {
        'title' : 'beritaku.id',
    }
    return HttpResponse(template.render(context, request))

def AboutUs(request) :
    template = loader.get_template('AboutUs.html')
    context = {
        'title' : 'beritaku.id',
    }
    return HttpResponse(template.render(context, request))

def Product(request) :
    template = loader.get_template('Product.html')
    context = {
        'title' : 'beritaku.id',
    }
    return HttpResponse(template.render(context, request))

def Wardah(request) :

    template = loader.get_template('Wardah.html')
    data = Data_Berita.objects.filter(kategori = 'Wardah')
    context = {
        'kategori' : 'Wardah',
        'data' : data
    }
    return HttpResponse(template.render(context, request))

def Implora(request) :

    template = loader.get_template('Implora.html')
    data = Data_Berita.objects.filter(kategori = 'Implora')
    context = {
        'kategori' : 'Implora',
        'data' : data
    }
    return HttpResponse(template.render(context, request))

def Maybelline(request) :

    template = loader.get_template('Maybelline.html')
    data = Data_Berita.objects.filter(kategori = 'Maybelline')
    context = {
        'kategori' : 'Maybelline',
        'data' : data
    }
    return HttpResponse(template.render(context, request))

def SeaMakeup(request) :

    template = loader.get_template('SeaMakeup.html')
    data = Data_Berita.objects.filter(kategori = 'SeaMakeup')
    context = {
        'kategori' : 'SeaMakeup',
        'data' : data
    }
    return HttpResponse(template.render(context, request))

def Makeover(request) :

    template = loader.get_template('Makeover.html')
    data = Data_Berita.objects.filter(kategori = 'Makeover')
    context = {
        'kategori' : 'Makeover',
        'data' : data
    }
    return HttpResponse(template.render(context, request))

def Shop(request) :
    template = loader.get_template('Shop.html')
    context = {
        'title' : 'beritaku.id',
    }
    return HttpResponse(template.render(context, request))

# def Login(request):
#     template = loader.get_template('Login.html')
#     context = {
#         'title' : 'beritaku.id',
#     }
#     return HttpResponse(template.render(context, request))

def Login(request):
   if request.method == "POST":
        emailku = request.POST.get("email")
        passwordku = request.POST.get("password")

        try:
            cekuser = Data_Pengguna.objects.get(email=emailku,password=passwordku)
            data = Data_Pengguna.objects.filter(email=emailku)
            for r in data:
               request.session['nama'] = r.nama
			   
            request.session['email'] = emailku
            request.session.save()
            return redirect("/beritaku/pengguna")
        except:
            return HttpResponse("""<script> alert("Username / Password Salah"); 
                  window.location.href = "/beritaku/login"; </script>""")
        
   return render(request, "login.html")

def Admin(request):
    template = loader.get_template('Admin.html')
    context = {
        'title' : 'beritaku.id',
    }
    return HttpResponse(template.render(context, request))

def Registrasi(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # form.save()
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to a home page or another page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'Registrasi.html', {'form': form})

# def pengguna(request):
#     template = loader.get_template('admin/pengguna.html')
#     context = {
#         'title' : 'beritaku.id',
#     }
#     return HttpResponse(template.render(context, request))

def pengguna(request) :
    if request.session.has_key('email'):
        email = request.session['email']
        nama = request.session['nama']
        return render(request,'admin/pengguna.html',{"email": email, "nama" : nama})
    else:
        return redirect("/beritaku/login")

# def lihatdata(request) :
#     template = loader.get_template('admin/lihatdata.html')
#     berita = Data_Berita.objects.all()
#     context = {
#         'title' : 'beritaku.id',
#         'data' : berita
#     }
#     return HttpResponse(template.render(context, request))

def lihatdata(request) :
    if request.session.has_key('email'):
        nama = request.session['nama']
        template = loader.get_template('admin/lihatdata.html')
        data = Data_Berita.objects.all()
        context = {
            'data' : data,
            'nama' : nama
        }
        return HttpResponse(template.render(context,request))
    else:
        return redirect("/beritaku/login")

# def lihatdata(request):
#     template = loader.get_template('lihatdata.html')
#     context = {
#         'title' : 'beritaku.id',
#     }
#     return HttpResponse(template.render(context, request))

# def keloladata(request):
#     form = DataBerita
#     template = loader.get_template('admin/keloladata.html')
#     context = {
#         'title' : 'beritaku.id',
#     }
#     return HttpResponse(template.render(context, request))

def keloladata(request):
	form = DataBerita(request.POST or None, request.FILES or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponse('<script> alert("Data berhasil disimpan"); window.location.href = "/beritaku/lihatdata"; </script>')
	pass
	return render(request,"admin/keloladata.html",{'form': form})

# def editdata(request, berita_id):
#     obj = get_object_or_404(Data_Berita, id = berita_id)

#     form = DataBerita(request.POST or None, instance = obj)
#     if form.is_valid():
#         form.save()
#         return redirect("/beritaku/lihatdata")
#     data = {
#         'dt':obj,
#     }
#     return render(request, 'admin/editdata.html', {'form': form})

def editdata(request, berita_id):
    obj = get_object_or_404(Data_Berita, id=berita_id)
    
    if request.method == 'POST':
        form = DataBerita(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            if 'gambar' in request.FILES:
                gambar = request.FILES['gambar']
                fs = FileSystemStorage()
                filename = fs.save(gambar.name, gambar)
                obj.gambar = fs.url(filename)
            form.save()
            return redirect("/beritaku/lihatdata")
    else:
        form = DataBerita(instance=obj)
    
    data = {
        'form': form,
        'dt': obj,
    }
    return render(request, 'admin/editdata.html', data)

def hapusdata(request, berita_id):
    try:
        berita = Data_Berita.objects.get(id=berita_id)
        berita.delete()
        return HttpResponse("""<script> alert ("Data Berhasil Dihapus"); window.location.href = "/beritaku/lihatdata";</script>""")

    except Data_Berita.DoesNotExist:
        raise Http404("Task Tidak Ditemukan")

def logout(request) :
    try:
        del request.session['email']
    except:
        pass
    return redirect("/beritaku/login")













# def sport(request) :
#     template = loader.get_template('sport.html')
#     data = Data_Berita.objects.filter(kategori = 'sport')
#     context = {
#         'title' : 'beritaku.id',
#         'kategori' : 'Sport',
#         'data' : data
#     }
#     return HttpResponse(template.render(context, request))

# def education(request) :
#     template = loader.get_template('education.html')
#     data = Data_Berita.objects.filter(kategori = 'education')
#     context = {
#         'title' : 'beritaku.id',
#         'kategori' : 'Education',
#         'data' : data
#     }
#     return HttpResponse(template.render(context, request))

# def login(request):
#    if request.method == "POST":
#         emailku = request.POST.get("email")
#         passwordku = request.POST.get("password")

#         try:
#             cekuser = Data_Pengguna.objects.get(email=emailku,password=passwordku)
#             data = Data_Pengguna.objects.filter(email=emailku)
#             for r in data:
#                request.session['nama'] = r.nama
			   
#             request.session['email'] = emailku
#             request.session.save()
#             return redirect("/beritaku/pengguna")
#         except:
#             return HttpResponse("""<script> alert("Username / Password Salah"); 
#                   window.location.href = "/beritaku/login"; </script>""")
        
#    return render(request, "login.html")

# def dashboard(request) :

#     template = loader.get_template('dashboard.html')
#     context = {
#         'title' : 'beritaku.id',
#     }
#     return HttpResponse(template.render(context, request))

# def pengguna(request) :
#     if request.session.has_key('email'):
#         email = request.session['email']
#         nama = request.session['nama']
#         return render(request,'admin/pengguna.html',{"email": email, "nama" : nama})
#     else:
#         return redirect("/beritaku/login")

# def lihatdata(request) :
#     if request.session.has_key('email'):
#         nama = request.session['nama']
#         template = loader.get_template('admin/lihatdata.html')
#         data = Data_Berita.objects.all()
#         context = {
#             'data' : data,
#             'nama' : nama
#         }
#         return HttpResponse(template.render(context,request))
#     else:
#         return redirect("/beritaku/login")

# def keloladata(request):
#     if request.session.has_key('email'):
#         nama = request.session['nama']
#         template = loader.get_template('admin/lihatdata.html')
#         data = Data_Berita.objects.all()
#         context = {
#             'data' : data,
#             'nama' : nama
#         }
#         return HttpResponse(template.render(context,request))
#     else:
#         return redirect("/beritaku/login")

	# form = DataBerita(request.POST or None, request.FILES or None)
	# if request.method == 'POST':
	# 	if form.is_valid():
	# 		form.save()
	# 		return HttpResponse('<script> alert("Data berhasil disimpan"); window.location.href = "/beritaku/lihatdata"; </script>')
	# pass
	# return render(request,"admin/keloladata.html",{'form': form})

# def logout(request) :
#     try:
#         del request.session['email']
#     except:
#         pass
#     return redirect("/beritaku/login")

# def hapusdata(request, berita_id):
#     try:
#         berita = Data_Berita.objects.get(id=berita_id)
#         berita.delete()
#         return HttpResponse("""<script> alert ("Data Berhasil Dihapus"); window.location.href = "/beritaku/lihatdata";</script>""")

#     except Data_Berita.DoesNotExist:
#         raise Http404("Task Tidak Ditemukan")

# def editdata(request, berita_id):
#     obj = get_object_or_404(Data_Berita, id = berita_id)

#     form = DataBerita(request.POST or None, instance = obj)
#     if form.is_valid():
#         form.save()
#         return redirect("/beritaku/lihatdata")
#     data = {
#         'dt':obj,
#     }
#     return render(request, 'admin/editdata.html', data)

# def detail(request, berita_id) :
#     template = loader.get_template('detail.html')
#     data = Data_Berita.objects.filter(id=berita_id)
#     context = {
#         'data' : data
#     }
#     return HttpResponse(template.render(context, request))
    


