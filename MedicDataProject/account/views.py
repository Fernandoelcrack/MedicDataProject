from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import SignUpForm, LoginForm, ProfileForm, PerfilForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt 
def index(request):
    return render(request, 'account/index.html')

@csrf_exempt 
def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect ('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render (request, 'account/register.html', {'form': form, 'msg':msg})

@csrf_exempt 
def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_patient:
                login(request, user)
                return redirect('patient')
            elif user is not None and user.is_doctor:
                login(request, user)
                return redirect('doctor')
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'account/login.html', {'form': form, 'msg': msg})

@csrf_exempt 
def admin(request):
    return render (request, 'account/adminpage.html')

@csrf_exempt 
def patient(request):
    return render (request, 'account/patient.html')

@csrf_exempt 
def doctor(request):
    return render (request, 'account/doctor.html')

@csrf_exempt 
def logoutUser (request):
    logout (request)
    return redirect('login_view')

@csrf_exempt 
def editorg(request):
    expgid = 0
    try:
        expgid = int(request.GET.get('expgid'))
    except:
        pass
    expedienteg = ExpedienteG.objects.filter(idEg = expgid)
    idDg = User.objects.get(id = request.user.id)
    print(idDg)
    expedientesg = ExpedienteG.objects.filter(idDg_id = idDg)


    
    if request.method == 'POST':
        expgid = int(request.POST.get('expgid'))
        nombreG = request.POST.get('nombreG')
        edadG = request.POST.get('edadG')
        peso = request.POST.get('peso')
        operaciones = request.POST.get('operaciones')
        lesiones = request.POST.get('lesiones')
        alergias = request.POST.get('alergias')
        enfermedades = request.POST.get('enfermedades')
        tipoSangre = request.POST.get('tipoSangre')
        idPg = request.POST.get('idPg')
        print(idPg)
        try:
            idPg = User.objects.get(username = idPg)
        except:
            pass
        print(idPg)
    
        if expedienteg.exists():
            expedienteg = ExpedienteG.objects.get(pk=expgid)
            expedienteg.nombreG = nombreG
            expedienteg.edadG = edadG
            expedienteg.peso = peso
            expedienteg.operaciones = operaciones
            expedienteg.lesiones = lesiones
            expedienteg.alergias = alergias
            expedienteg.enfermedades = enfermedades
            expedienteg.tipoSangre = tipoSangre
            expedienteg.idPg = idPg
            expedienteg.idDg = idDg
            expedienteg.save()
            print('1', expedienteg.idEg)
            return redirect('/expedienteg?expgid=%i' % expgid) 
        else:
            expedienteg = ExpedienteG.objects.create(nombreG=nombreG, edadG=edadG, peso=peso, operaciones=operaciones, lesiones=lesiones, alergias=alergias, enfermedades=enfermedades, tipoSangre=tipoSangre, idPg=User.objects.get(username = idPg), idDg=idDg) 

            return redirect('/expedienteg?expgid=%i' % expedienteg.idEg)

        
    if expgid > 0:
        expedienteg = ExpedienteG.objects.get(pk=expgid)
    else:
        expedienteg = ''

    context = {
        'expgid': expgid,
        'expedientesg' : expedientesg,
        'expedienteg' : expedienteg,
    }

    return render(request, 'account/expedienteg.html', context)

@csrf_exempt 
def editoro(request):
    expoid = 0
    try:
        expoid = int(request.GET.get('expoid'))
    except:
        pass
    expedienteo = ExpedienteO.objects.filter(idEo = expoid)
    idDo = User.objects.get(id = request.user.id)
    expedienteso = ExpedienteO.objects.filter(idDo_id = idDo)

    if request.method == 'POST':
        expoid = int(request.POST.get('expoid'))
        nombreO = request.POST.get('nombreO')
        edadO = request.POST.get('edadO')
        gojoD = request.POST.get('gojoD')
        gojoI = request.POST.get('gojoI')
        padecimientos = request.POST.get('padecimientos')
        cambioMicas = request.POST.get('cambioMicas')
        idPg = request.POST.get('idPg')

        if expedienteo.exists():
            #expedienteo = ExpedienteO.objects.get(pk=expoid)
            expedienteo.nombreO = nombreO
            expedienteo.edadO = edadO
            expedienteo.gojoD = gojoD
            expedienteo.gojoI = gojoI
            expedienteo.padecimientos = padecimientos
            expedienteo.cambioMicas = cambioMicas
            expedienteo.idPg = User.objects.get(username = idPg)
            expedienteo.idDo = idDo
            expedienteo.save()

            return redirect('/expedienteo?expoid=%i' % expoid)
        else:
            expedienteo = ExpedienteO.objects.create(nombreO=nombreO, edadO=edadO, gojoD = gojoD, gojoI = gojoI, padecimientos = padecimientos, cambioMicas = cambioMicas, idPg=User.objects.get(username = idPg), idDo=idDo)  

            return redirect('/expedienteo?expoid=%i' % expedienteo.idEo)

    if expoid > 0:
        expedienteo = ExpedienteO.objects.get(pk=expoid)
    else:
        expedienteo = ''

    context = {
        'expoid': expoid,
        'expedienteso' : expedienteso,
        'expedienteo' : expedienteo,
    }
    return render(request, 'account/expedienteo.html', context)


@csrf_exempt 
def delete_expedienteg(request, expgid):
    expedienteg = ExpedienteG.objects.get(pk=expgid)
    expedienteg.delete()

    return redirect('expedienteg')

@csrf_exempt 
def delete_expedienteo(request, expoid):
    expedienteo = ExpedienteO.objects.get(pk=expoid)
    expedienteo.delete()
    return redirect('expedienteo')

@csrf_exempt 
def delete_expediented(request, expdid):
    expediented = ExpedienteD.objects.get(pk=expdid)
    expediented.delete()

    return redirect('expediented')

@csrf_exempt 
def accountSettingsMedic(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
    
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
    
    return render(request, 'account/account_settings.html', {'form': form})

@csrf_exempt 
def viewExpediente(request):
    user_id = request.user.id
    expediente = ExpedienteG.objects.filter(idPg = user_id)
    expediented = ExpedienteD.objects.filter(idPg = user_id)
    expedienteo = ExpedienteO.objects.filter(idPg = user_id)
    

    context = {
        "expediente": expediente,
        "expedienteo": expedienteo,
        "expediented": expediented,
    
    }
    return render (request, "account/patient.html", context)

@csrf_exempt 
def accountSettingsPatient(request):
    try:
        perfil = request.user.perfil
    except Perfil.DoesNotExist:
        perfil = Perfil(user=request.user)
    
    form = PerfilForm(instance=perfil)
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
    
    return render(request, 'account/account_settingsP.html', {'form': form})


@csrf_exempt 
def editord(request):
    expdid = 0
    try:
        expdid = int(request.GET.get('expdid'))
    except:
        pass
    expediented = ExpedienteD.objects.filter(idEd = expdid)
    idDd = User.objects.get(id = request.user.id)
    expedientesd = ExpedienteD.objects.filter(idDd_id = idDd)

    if request.method == 'POST':
        expdid = int(request.POST.get('expdid'))
        nombreD = request.POST.get('nombreD')
        edadD = request.POST.get('edadD')
        NDiente1 = request.POST.get('NDiente1')
        NDiente2 = request.POST.get('NDiente2')
        NDiente3 = request.POST.get('NDiente3')
        NDiente4 = request.POST.get('NDiente4')
        NDiente5 = request.POST.get('NDiente5')
        Descripcion = request.POST.get('Descripcion')
        idPg = request.POST.get('idPg')
        print(idPg)
        idPg = User.objects.get(username = idPg)
        print(idPg)
    
        if expediented.exists():
            #expediented = ExpedienteD.objects.get(pk=expdid)
            expediented.nombreD = nombreD
            expediented.edadD = edadD
            expediented.NDiente1 = NDiente1
            expediented.NDiente2 = NDiente2
            expediented.NDiente3 = NDiente3
            expediented.NDiente4 = NDiente4
            expediented.NDiente5 = NDiente5
            expediented.Descripcion = Descripcion
            expediented.idPg = idPg
            expediented.idDd = idDd
            expediented.save()
            print('1', expediented.idEd)
            return redirect('/expediented?expdid=%i' % expdid) 
        else:
            expediented = ExpedienteD.objects.create(nombreD=nombreD, edadD=edadD, NDiente1=NDiente1, NDiente2=NDiente2, NDiente3=NDiente3, NDiente4=NDiente4, NDiente5=NDiente5, Descripcion=Descripcion, idPg=User.objects.get(username = idPg), idDd=idDd)  

            return redirect('/expediented?expdid=%i' % expediented.idEd)
        
    if expdid > 0:
        expediented = ExpedienteD.objects.get(pk=expdid)
    else:
        expediented = ''

    context = {
        'expdid': expdid,
        'expedientesd' : expedientesd,
        'expediented' : expediented,
    }

    return render(request, 'account/expediented.html', context)



class Error404View(TemplateView):
    template_name = "account/error_404.html"



class Error500View(TemplateView):
    template_name = "account/error_500.html"
    @classmethod
    def as_error_view(cls):
        v=cls.as_view()
        def view(request):
            r=v(request)
            r.render()
            return r
        return view
