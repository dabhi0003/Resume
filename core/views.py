from django.shortcuts import render,redirect
from django.views import View
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
class Form(View):
    def get(self,request):
        return render(request,"resume-form.html")

    def post(Sef,request):
        if request.user.is_authenticated:
            user=request.user
            firstname=request.POST['first_name']
            lastname=request.POST['last_name']
            number=request.POST['contact_number']
            email=request.POST['email']
            address=request.POST['address']
            github_link=request.POST['github_link']
            linkedin_link=request.POST['linkedin_link']
            image=request.FILES['image']
            professional_summary=request.POST['professional_summary']
            degree=request.POST['degree']
            institution=request.POST['institution']
            int_address=request.POST['int_address']
            year=request.POST['year']
            courses=request.POST['courses']
            job_title=request.POST['job_title']
            company=request.POST['company']
            location=request.POST['location']
            start_date=request.POST['start_date']
            end_date=request.POST['end_date']
            description=request.POST['description']
            name=request.POST['name']
            title=request.POST['title']
            project_description=request.POST['project_description']
            technologies=request.POST['technologies']

            data=Resume(user=user,first_name=firstname,last_name=lastname,contact_number=number,email=email,address=address,
                        github_link=github_link,linkedin_link=linkedin_link,professional_summary=professional_summary,degree=degree,
                        institution=institution,int_address=int_address,year=year,courses=courses,job_title=job_title,company=company,
                        location=location,start_date=start_date,end_date=end_date,description=description,name=name,title=title,
                        project_description=project_description,technologies=technologies,image=image)
            data.save()
            return redirect("all-templates")
        else:
            return redirect("login")
    
class LoginView(View):
    def get(self,request):
        return render(request,"login.html")

    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']

        check_user = authenticate(username=username, password=password)
        if check_user:
            login(request, check_user)
            messages.success(request,"login successfully..........")  
            return redirect('home')
        else:
            messages.info(request,'Some Field are Empty.....!!!')
            return redirect("login1")

class Register(View):
    def get(self,request):
            return render(request,"register.html")
    def post(self,request):
            usr=User.objects.create_user(username=request.POST['username'],email=request.POST['email'])
            usr.set_password(request.POST['password'])
            usr.save()  
            messages.success(request,"User created successfully....")  
            return redirect("login")
    
class Home(View):
    def get(self,request):
        return render(request,"home.html")
    

    
def logoutView(request):
    logout(request)
    return redirect("login")


class TemplateView(View):
    def get(self, request):
        details = Resume.objects.latest('id')
        return render(request, "template1.html", {"details": [details]})



class TemplateView2(View):
    def get(self,request):
        details=Resume.objects.latest('id')
        return render(request,"template2.html",{"details":[details]})
    

class TemplateView3(View):
    def get(self,request):
        details=Resume.objects.latest("id")
        return render(request,"template3.html",{"details":[details]})


class AllTemplate(View):
    def get(self,request):
        return render(request,"all_templates.html")
    

