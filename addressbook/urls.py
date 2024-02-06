"""addressbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# In your urls.py file
from django.urls import path
from addresses.views import AddressDetailView,AddressCreateView,AddressWithinRangeView,AddressListView

urlpatterns = [
    path('api/addresses/', AddressListView.as_view(), name='address-list'),
    path('api/addresses/<int:pk>/', AddressDetailView.as_view(), name='address-detail'),
    path('api/addresses/create/', AddressCreateView.as_view(), name='address-create'),
    path('api/addresses/within-range/<int:latitude>/<int:longitude>/', AddressWithinRangeView.as_view(),
         name='address-within-range'),

]
