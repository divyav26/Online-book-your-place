from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('all-news',views.all_news,name='all-news'),
    path('all-category',views.all_category,name='all-category'),
    path('category/<int:id>',views.category,name='category'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('payment/',views.payment,name='payment'),
    #path('add_people/',views.add_people,name='add_people'),
    path('signup/',views.signup ),
    path('create/', views.createInvoice, name="invoice-create"),
    path('customer_list/',views.customer_list,name='customer_list'),
    path('contact/',views.contact,name='contact'),
    path('accounts/',include('django.contrib.auth.urls'))


    # path('ca',views.state,name='home'),
    # path('category/<int:id>',views.category,name='category'),

]
