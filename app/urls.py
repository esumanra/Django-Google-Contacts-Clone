from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    # path('detail/<int:id>', views.detail, name='detail'),
    # path('search/', views.search, name='search'),
    path('', views.HomePageView.as_view(), name='home'),
    path('detail/<int:pk>/', views.DetailPageView.as_view(), name='detail'),
    path('search/', views.SearchContactView.as_view(), name='search'),
    path('contact/create', views.CreateContactView.as_view(), name='create'),
    path('contact/update/<int:pk>',
         views.UpdateContactView.as_view(), name='update'),
    path('contact/delete/<int:pk>',
         views.DeleteContact.as_view(), name='delete'),
    path('signup', views.SignUpView.as_view(), name='signup')
]
