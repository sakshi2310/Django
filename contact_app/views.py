from django.shortcuts import render,redirect
from contact_app.models  import user,contacts,UserForm,ContactForm
from django.contrib import messages
from django.core.mail import  send_mail
from contact_book.settings import *
# Create your views here.


def register(request):
     userFormobj = UserForm()
     if 'Register' in request.POST:
          # email = request.POST.get('email')
          userFormobj = UserForm(request.POST)

          # if userFormobj.is_valid():
          #      print("hello")
          #      email = userFormobj.cleaned_data['email']
          #      otp = "1234"
          #      send_mail("user data = ",f"Verify your mail by the opt: /n{otp}","from@example.com",[email],fail_silently=False)
          #      messages.success(request,"user saved sussesfully")
          #      userFormobj.save()
          # else:
          #      messages.error(request,userFormobj.errors)

          userFormobj.save()
     return render(request,'register.html',{'userfrm':userFormobj})

def login(request):
     mes = ''

     if 'user_id' in request.session:
          return redirect('/view_contact')
     if 'login' in request.POST:
          email = request.POST['email']
          password = request.POST['password']
          obj = user.objects.filter(email=email,password=password)
          if obj.count() == 1:
               print("success")
               row = obj.get()
               request.session['user_id'] =row.id
               request.session['user_name'] = row.name
               return redirect("/view_contact")
          else:
               print("fail")
               mes = 'invaild email or password..'
     return render(request,'login.html',{'mes': mes}) 

def logout(request):
     del request.session['user_id']
     return redirect('/login')
def add_contact(request):
     s = 'suceess'
     user_id = request.session['user_id']
     admin_name = request.session['user_name']
     ContactFormObj = ContactForm()
     if 'save' in request.POST:
          
          print(user_id)
          ContactFormObj = ContactForm(request.POST)
          ContactFormObj.save()
         
          return redirect('/view_contact')

     return render(request,'add_contact.html',{'user_id':int(user_id),'admin_name':admin_name,'ContactFrm':ContactFormObj})

def view_contact(request):
     # contacts.objects.all().delete()
     if 'user_id' not in request.session:
          return redirect('/login')
     admin_name = request.session['user_name']
     users = contacts.objects.filter(user_id=request.session['user_id'])
     return render(request,'view_contact.html',{'users':users,'admin_name':admin_name})

def edit_data(request,edit_id):
     obj = contacts.objects.filter(id=edit_id).get()
     user_id = request.session['user_id']
     ContactFormObj = ContactForm(instance=obj)
     if 'save' in request.POST:
          ContactFormObj = ContactForm(request.POST,instance=obj)
          ContactFormObj.save()
          return redirect('/view_contact')

     return render(request,'add_contact.html',{'obj':obj,'user_id':int(user_id),'ContactFrm':ContactFormObj})

def del_data(request,del_id):
     obj = contacts.objects.filter(id = del_id).delete()
     return redirect('/view_contact')

def edit_user(request):
     obj = user.objects.filter(id=request.session['user_id']).get()
     user_id = request.session['user_id']
     admin_name = request.session['user_name']
     userFornObj = UserForm(instance=obj)
     if 'save' in request.POST:
          userFornObj = UserForm(request.POST,instance=obj)
          userFornObj.save()
          return redirect('/view_contact')

     return render(request,'edit_user.html',{'obj':obj,'user_id':int(user_id),'admin_name':admin_name,'userFrm':userFornObj})

def admin_confirmation(request):
     mes = ''
     admin_name = request.session['user_name']
     if 'save' in request.POST:
          old_password = request.POST['password']

          obj=user.objects.filter(id=request.session['user_id']).get()
          print(obj)
          if obj.password == old_password:
               return redirect('/edit_user')
          else:
               mes = 'invalid password please try again..'

     return render(request,'admin_confirmation.html',{'mes':mes,'admin_name':admin_name})


def header(request):
     # admin = user.objects.filter(id = request.session['user_id']).get()
     return render(request,'header.html')