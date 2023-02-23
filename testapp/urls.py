from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('contact/',views.contact, name='contact'),
    path('all-news',views.all_news,name='all-news'),
    path('all-category',views.all_category,name='all-category'),
    path('category/<int:id>',views.category,name='category'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('payment/',views.payment,name='payment'),
    path('add_people/',views.add_people,name='add_people'),
    path('signup/',views.signup ),
    #path('search/',views.search_state,name='search_state'),
    path('accounts/',include('django.contrib.auth.urls'))


    # path('ca',views.state,name='home'),
    # path('category/<int:id>',views.category,name='category'),

]
