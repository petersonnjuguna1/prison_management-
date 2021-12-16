from django.http import request
from django.shortcuts import render,redirect
from .models import *
from .forms import *
#from .filter import *
#from .decorators import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils.regex_helper import Group
from django.contrib.auth.models import Group

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter



# generation of reports  

def prisonerpdf(request):
    #create a buytestream buffer
    buf = io.BytesIO()
    #create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    #create a text object
    textobj = c.beginText()
    textobj.setTextOrigin(inch, inch)
    textobj.setFont("Helvetica", 14)
    
    prisoners=Prisonerdetails.objects.filter(user=request.user.id) 
    lines = []
    
    for prisoner in prisoners:
        lines.append(prisoner.fullname)
        lines.append(prisoner.PNo)
        lines.append(prisoner.offence)
        lines.append(prisoner.sentence)
        lines.append(prisoner.datein)
        lines.append(prisoner.dateout)
        lines.append("****************************************************")
        
    for line in lines:
        textobj.textLine(str(line))
    
    c.drawText(textobj)
    c.showPage()
    c.save()
    buf.seek(0)
    
    return FileResponse(buf, as_attachment=True, filename='prisonerpdf.pdf')


def visitorpdf(request):
    #create a buytestream buffer
    buf = io.BytesIO()
    #create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    #create a text object
    textobj = c.beginText()
    textobj.setTextOrigin(inch, inch)
    textobj.setFont("Helvetica", 14)
    
    visits=Visitation.objects.all() 
    lines = []
    
    for visit in visits:
        lines.append(visit.visitor)
        lines.append(visit.visitationdate)
        # lines.append(visit.telno)
        lines.append(visit.Prisonernumber)
        lines.append(visit.date)
        lines.append(visit.status)
        lines.append("********************************************************")
        
    for line in lines:
        textobj.textLine(str(line))
    
    c.drawText(textobj)
    c.showPage()
    c.save()
    buf.seek(0)
    
    return FileResponse(buf, as_attachment=True, filename='visitorpdf.pdf')
        
    


# Create your views here.

def home(request):
    return render(request,'users/home.html')

def about(request):
    return render(request,'users/about.html')

def contact(request):
    return render(request,'users/contact.html')

def signout(request):
    #signout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect('home')

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!!!")
    return redirect("/")
    





def prisonerlogin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        
        if user is not None:
            login(request, user)
            return redirect('prisonerdetails')
        else:
            messages.info(request, 'Username and password didn`t match. Try Again!!!')
    
    return render(request, 'users/prisoners/prisonerlogin.html')

def prisonersignup(request):
    return render(request,'users/prisoners/prisonersignup.html')

def prisonerreg(request):
    #calls created form
    if request.method == 'POST':
        form = PrisonerRegForm(request.POST)
                                                
        if form.is_valid(): #if form is valid, save to database
            user=form.save()
            user.refresh_from_db()
            # user.prisonerprofile.email=form.cleaned_data.get('email')#making the email valid and storing it to database
            # user.prisonerprofile.phoneno=form.cleaned_data.get('phoneno')
            group=Group.objects.get(name='prisoner')
            user.groups.add(group)
            user.save()
            form.save()

            username=form.cleaned_data.get('username')#stores registered details and login directly
            password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=password) #checks whether the details are valid
            login(request,user)
            messages.success(request, "registration successful.")
            return redirect('prisonerdashboard')        
        messages.error(request, "registration was unsuccessful. Try again!!!")
    else:
        form= PrisonerRegForm() 
    context={'form':form}  #is a variable that holds a form (context dictionary)
    return render(request,'users/prisoners/prisonerreg.html',context)

def pcreate(request):
    form=CreatePrisonerForm()
    prison=Prisonerdetails.objects.all() 
    if request.method =='POST':
        form=CreatePrisonerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prisonerdashboard')
    form=CreatePrisonerForm (initial={'user':request.user.id} | {'prisoner':request.user.id})
    context={'form':form,'prison':prison}
    return render(request, 'users/Prisoners/pcreate.html', context)

def pupdate(request,pk):
    prison=Prisonerdetails.objects.get(id=pk)
    form=CreatePrisonerForm(instance=prison)
    if request.method == 'POST':
        form=CreatePrisonerForm(request.POST,instance=prison)
        if form.is_valid:
            form.save()
            return redirect('pcreate')
    context={'form':form}
    return render(request,'users/Prisoners/pcreate.html',context)

def pdelete(request,pk):
    prison=Prisonerdetails.objects.get(id=pk)
    if request.method == 'POST':
        pcreate.delete()
        return redirect('pcreate')
    context={'prison':prison}

    return render(request,'users/Prisoners/pcreate.html',context)

def prisonerdashboard(request):
    return render(request,'users/prisoners/prisonerdashboard.html')

def prisonersreport(request):
    prisoners=Prisonerdetails.objects.filter(user=request.user.id) 
   
    context={'prisoners':prisoners}
    return render(request,'users/prisoners/prisonersreport.html',context)

def prisonersaccount(request):
    return render(request,'users/prisoners/prisonersaccount.html')

def psettingaccount(request):
    prisoner=request.user.prisonerprofile
    form=PrisonerAccountForm(instance=prisoner)
    if request.method=='POST':
        form=PrisonerAccountForm(request.POST,request.FILES,instance=prisoner)
        if form.is_valid:form.save()
        return redirect('prisonersaccount')
     
    context={'form':form,}        
    return render(request,'users/Prisoners/psettingaccount.html', context)








def vregister(request):
        #calls created form
    if request.method == 'POST':
        form = VisitorRegForm(request.POST)
        #if form is valid, save to database
        if form.is_valid(): 
            user=form.save()
            user.refresh_from_db()
            # user.visitorsprofile.email=form.cleaned_data.get('email')#making the email valid and storing it to database
            # user.visitorsprofile.phoneno=form.cleaned_data.get('phoneno')
            group=Group.objects.get(name='visitor')
            user.groups.add(group)
            user.save()
            form.save()

            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request, "Login successfully." )
            return redirect('vcreate')
    else:
        form= VisitorRegForm() 
    context={'form':form}  #is a variable that holds a form (context dictionary)
    return render(request,'users/visitors/vregister.html',context)

def vlogin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        
        if user is not None:
            login(request, user)
            return redirect('vcreate')
        else:
            messages.info(request, 'Username and password didn`t match. Try Again!!!')
    
    return render(request, 'users/visitors/vlogin.html')

def vcreate(request):
    form=CreateVisitationForm()
    visits=Visitation.objects.all() 
    if request.method =='POST':
        form=CreateVisitationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vcreate')
    visits=Visitation.objects.filter(user=request.user.id) 
    form=CreateVisitationForm (initial={'user':request.user.id} | {'visitor':request.user.id})
    context={'form':form,'visits':visits}
    return render(request, 'users/visitors/vcreate.html', context)


def vupdate(request,pk):
    visit=Visitation.objects.get(id=pk)
    form=CreateVisitationForm(instance=visit)
    if request.method == 'POST':
        form=CreateVisitationForm(request.POST,instance=visit)
        if form.is_valid:
            form.save()
            return redirect('vcreate')
    context={'form':form}
    return render(request,'users/visitors/vcreate.html',context)

def vdelete(request,pk):
    visitation=Visitation.objects.get(id=pk)
    if request.method == 'POST':
        visitation.delete()
        return redirect('/vcreate')
    context={'visitation':visitation}
    return render(request,'users/visitors/vdelete.html',context)


def visitorsdashboard(request):
    visitor=Visitation.objects.all()
    total_visitors=visitor.count()
    visits=Visitation.objects.all() 
    
    context={'visits':visits}
    
    return render(request,'users/visitors/visitorsdashboard.html',context)

def visitorsreport(request):
    visits=Visitation.objects.all() 
    context={'visits':visits}

    return render(request,'users/visitors/visitorsreport.html',context)

def visitorsaccount(request):
    return render(request,'users/visitors/visitorsaccount.html')



def settingaccount(request):
    visitor=request.user.visitorsprofile
    form=VisitorAccountForm(instance=visitor)
    if request.method=='POST':
        form=VisitorAccountForm(request.POST,request.FILES,instance=visitor)
        if form.is_valid():
            form.save()
        return redirect('visitorsaccount')
    
    context={'form':form,}        
    return render(request,'users/visitors/settingaccount.html', context)

def viewvisitation(request):
   
    visits=Visitation.objects.all() 
   
    context={'visits':visits}
    return render(request, 'users/prisoners/newvisits.html', context)

def prisonerdetails(request):
    form=CreatePrisonerForm()
    # visits=Visitation.objects.all() 
    if request.method =='POST':
        form=CreatePrisonerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prisonerdetails')
    prisoners=Prisonerdetails.objects.filter(user=request.user.id) 
    form=CreatePrisonerForm(initial={'user':request.user.id} | {'prisoners':request.user.id})
    context={'form':form,'prisoners':prisoners}
    
  
    return render(request, 'users/prisoners/prisoners.html', context)






def prisonerupdate(request,pk):
    prisoner=Prisonerdetails.objects.get(id=pk)
    form=CreatePrisonerForm(instance=prisoner)
    if request.method == 'POST':
        form=CreatePrisonerForm(request.POST,instance=prisoner)
        if form.is_valid:
            form.save()
            return redirect('prisonerdetails')
    context={'form':form}
    return render(request,'users/Prisoners/prisoners.html',context)



def prisonerdelete(request,pk):
    prisoner=Prisonerdetails.objects.get(id=pk)
    if request.method == 'POST':
        prisoner.delete()
        return redirect('prisonerdetails')
    context={'prisoner':prisoner}
    
    return render(request,'users/Prisoners/prisonerdelete.html',context)


def approve(request,pk):
    visit=Visitation.objects.all()
    visit=Visitation.objects.get(id=pk)
    visit.status='Approved'
    visit.save()
    return HttpResponseRedirect('/viewvisitation')
    
    

def reject(request,pk):
    visit=Visitation.objects.all()
    visit=Visitation.objects.get(id=pk)
    visit.status='Rejected'
    visit.save()
    return HttpResponseRedirect('/viewvisitation')