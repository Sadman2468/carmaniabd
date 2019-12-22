from django.shortcuts import render
from .forms import Contact_form,Giverent_form               #form_post
from .models import sell_car_post,Giverent_field,car_choose,User_rent_form
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView #UpdateView
from users.models import User_profile
from django.contrib import messages
# Create your views here.
def home_page(request):

    return render(request,'blog/index.html')

def contact(request):

    if(request.method=='POST'):
        form = Contact_form(request.POST or None)
        if(form.is_valid()):
            form.save()
            form = Contact_form()
            messages.success(request,'succesfully posted !')
    else:
        form = Contact_form()
    return render(request,'blog/contact.html',{'form':form})

def rent(request):

    return render(request,'blog/rent.html')

def selfdriven(request):

    return render(request,'blog/selfdriven.html')

# def takerent(request):
#
#     return render(request,'blog/takerent_list.html')

def giverent(request):

    if(request.method=='POST'):
        form = Giverent_form(request.POST , request.FILES)
        if(form.is_valid()):
            form.save()
            form = Giverent_form()
            messages.success(request,'succesfully posted !')
    else:
        form = Giverent_form()
    return render(request,'blog/giverent.html',{'form':form})
# @login_require
# def sellcar(request):
#
#     if(request.method == "POST"):
#         form = form_post(request.POST or None)
#         if(form.is_valid()):
#             form.save()
#             form = form_post()
#
#     else:
#         form = form_post()
#
#     # value = sell_car_post.objects.all()
#
#     return render(request,'blog/sellcar.html',{'form':form})




# def sellcar_post(request):
#
#     value = sell_car_post.objects.all()
#
#     context = {
#         'data': value
#     }
#     return render(request,'blog/buycar.html',context)

class BuyCarListView(ListView):

    model = sell_car_post
    template_name = 'blog/buycar_list.html'
    context_object_name = 'post'

    # def get_context_data(self,**kwargs):
    #     context = super(BuyCarListView,self).get_context_data(**kwargs)
    #     context['post'] = sell_car_post.objects.all()
    #     return context

class TakeRentListView(ListView):

    model = Giverent_field
    template_name = 'blog/takerent_list.html'
    context_object_name = 'post'


class TakeRentDetailView(DetailView):
    model = Giverent_field

class ChooseCarListView(ListView):
    model = car_choose
    template_name = 'blog/choose_car_list.html'
    context_object_name = 'post'

class ChooseCarDetailView(DetailView):
    model = Giverent_field

class BuyCarDetailView(DetailView):
    model = sell_car_post
    # fields = ['image']

class SellCarCreateView(LoginRequiredMixin,CreateView):
    model = sell_car_post
    fields = ['car_name','engine_capacity','model','color','seat_capacity','price','image']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
def User_f(request):
    post = User_rent_form(request.POST , request.FILES)
    if(request.method=='POST' and request.method=='FILES'):

        fname = request.Post.get('fname')
        lname = request.Post.get('lname')
        phone = request.Post.get('phone')
        rent_date = request.Post.get('rent_date')
        duration = request.Post.get('duration')
        upload_lic = request.FILES.get('upload_lic')
        messages.success(request,'succesfully posted !')

        post = User_rent_form(fname=fname,lname=lname,phone=phone,rent_date=rent_date,duration=duration,upload_lic=upload_lic)
        post.save()          
        
        return render(request,'blog/reg_form.html',{post:post})
    return render(request,'blog/reg_form.html')
