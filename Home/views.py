
from django.shortcuts import render,HttpResponse,redirect
from Home.models import Contact, Product,Logo
from django.core.paginator import Paginator
from datetime import datetime
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User,auth
from datetime import datetime

# Create your views here.
def home(request):
    pro= Product.objects.all()
    logo=Logo.objects.all()
    forpaginator=Paginator(pro,4)
    pageNumber=request.GET.get('page')
    pro_final=forpaginator.get_page(pageNumber)
    totalPage=pro_final.paginator.num_pages
    
    #for insert_msg and date

    date=datetime.now()
    msg=None
    h=int(date.strftime('%H'))

    if h<12:
        msg="gd mrg"
    elif h<16:
        msg="gd afternoon"
    elif h<21:
        msg="gd even"
    else:
        msg="gd ni8"
    
    
    context={
           "product":pro,
           'pros':pro_final,
           'totalPageList':[n+1 for n in range(totalPage)],
           'insert_date':date,  #for insert_msg and date
        'insert_msg':msg ,  #for insert_msg and date
        "logos":logo
    } 
    return render(request,"home.html",context)

def about(request):
        return render(request,"about.html")




def service(request):
        '''pro= Product.objects.all()
        forpaginator=Paginator(pro,4)
        pageNumber=request.GET.get('page')
        pro_final=forpaginator.get_page(pageNumber)
        totalPage=pro_final.paginator.num_pages
        y=[n+1 for n in range(totalPage)]'''
        ''' allprods =[[pro_final,y],[pro_final,y]]
       context={
               'allprods':allprods
        }
        '''
        allprods=[]
        catprods = Product.objects.values('category','id')
        cats={item['category'] for item in catprods }
        for cat in cats:
              pro=Product.objects.filter(category=cat)
              forpaginator=Paginator(pro,4)
              pageNumber=request.GET.get('page')
              pro_final=forpaginator.get_page(pageNumber)
              totalPage=pro_final.paginator.num_pages
              y=[n+1 for n in range(totalPage)]
              allprods.append([pro_final,y])

        context={
          # "product":pro,
          # 'pros':pro_final,
          # 'totalPageList':y,
            'allprods':allprods
         }
        return render(request,"service.html",context)

def contact(request):
        if request.method =="POST":
               name=request.POST['name']
               email=request.POST['email']
               phone=request.POST['phone']
               discription =request.POST['discription']
               if len(name)<1 or len(email) <3 or len(phone) < 4 :
                      messages.error(request,"Oops......plz recheck details")
               else:
                      getDetails= Contact (name=name,email=email,phone=phone,discription=discription)
                      messages.success(request,"Thank you for response")
                      getDetails.save()
        
        return render(request,"contact.html")

def Detailpage(request,ilabel):
      
        pro1= Product.objects.get(product_name=ilabel)
        logo=Logo.objects.all()
      

        con={
            "pro11":pro1  ,
            "logos":logo
            

        }
        return render(request,"detail.html",con)
        




def search (request):
    if request.method =='GET':
        nameName=request.GET.get('nameName')

        stu=Product.objects.all()
        if nameName :
            stu=stu.filter(Q(product_name__icontains=nameName) | Q(category__icontains=nameName) | Q(price__icontains=nameName))
        
        context={
            'stu':stu,
            'nameName':nameName  
        }
        return render(request, 'search.html',context)
    
    return HttpResponse('doesnot search')

def signpin(request):
      return render(request,"login.html")

def login(request):
    if request.method=="POST":
        username_1=request.POST["username2"]
        password_1=request.POST["password2"]

        uvw=auth.authenticate(username=username_1,password=password_1)

        if uvw is not None:
            auth.login(request,uvw)
            return redirect ('/')
        else:
            messages.error(request,"invalid credentials")
            return redirect("login")
        
    return redirect('/')


def logout(request):
    auth.logout(request)
    return redirect('/')



def register(request):
    if request.method=="POST":
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        username=request.POST["username"]
        email_id=request.POST["email_id"]
        pass1=request.POST["pass1"]
        pass2=request.POST["pass2"]
        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"usernmse already registerd")
                return redirect('/')
            elif User.objects.filter(email=email_id).exists():
                messages.info (request,"Email_id already registered")
                return redirect('/')


            else:
                xyz=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email_id,password=pass1) #,last_login=datetime.now()
                xyz.save()
                print("registration done")
                return redirect('/')
        else:
            print("password doesn't matched")
            messages.info (request,"password doesn't matched")

        return redirect("/")


