from django.urls import path
from .views import AddressListView, AddressDetailView, AddressCreateView,AddressWithinRangeView

urlpatterns = [
    path('api/addresses/', AddressListView.as_view(), name='address-list'),
    path('api/addresses/<int:pk>/', AddressDetailView.as_view(), name='address-detail'),
    path('api/addresses/create/', AddressCreateView.as_view(), name='address-create'),
    path('api/addresses/within-range/<int:latitude>/<int:longitude>/', AddressWithinRangeView.as_view(), name='address-within-range')

]
