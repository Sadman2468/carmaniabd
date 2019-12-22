from django.urls import path,register_converter
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import ListView
from .views import BuyCarListView,BuyCarDetailView, SellCarCreateView,TakeRentListView,TakeRentDetailView,ChooseCarListView,ChooseCarDetailView

app_name = 'blog'
urlpatterns = [
    path('', views.home_page,name='home_page'),
    path('contact/',views.contact,name='contact' ),
    path('rent/',views.rent,name='rent' ),
    path('giverent/',views.giverent,name='giverent' ),
    #path('takerent/',views.takerent,name='takerent' ),
    path('selfdriven/',views.selfdriven,name='selfdriven' ),
    # path('sell-car/',views.sellcar,name='sellcar' ),

    path('sell-car/',SellCarCreateView.as_view(),name='sellcar' ),
    path('takerent/',TakeRentListView.as_view(),name='takerent' ),
    path('choose_car/',ChooseCarListView.as_view(),name='choose_car' ),
    path('choose_car/<int:pk>',ChooseCarDetailView.as_view(),name='detail1' ),
    path('takerent/<int:pk>',TakeRentDetailView.as_view(),name='detail1' ),
    # path('post/<int:pk>/update/',PostUpdateView.as_view(),name='update' ),
    path('buy-car/',BuyCarListView.as_view(),name='buycar' ),
    path('post/<int:pk>/',BuyCarDetailView.as_view(),name='detail' ),
    path('user_form_car/',views.User_f,name='User_f' ),
]
