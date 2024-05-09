# models.py

from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True)

# serializers.py

from rest_framework import serializers
from .models import Vendor, PurchaseOrder

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

# views.py

from rest_framework import generics
from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer

class VendorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

# urls.py

from django.urls import path
from .views import (
    VendorListCreateAPIView,
    VendorRetrieveUpdateDestroyAPIView,
    PurchaseOrderListCreateAPIView,
    PurchaseOrderRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('api/vendors/', VendorListCreateAPIView.as_view(), name='vendor-list'),
    path('api/vendors/<int:pk>/', VendorRetrieveUpdateDestroyAPIView.as_view(), name='vendor-detail'),
    path('api/purchase_orders/', PurchaseOrderListCreateAPIView.as_view(), name='purchaseorder-list'),
    path('api/purchase_orders/<int:pk>/', PurchaseOrderRetrieveUpdateDestroyAPIView.as_view(), name='purchaseorder-detail'),
]

# authentication.py

from rest_framework.authentication import TokenAuthentication

class CustomAuthentication(TokenAuthentication):
    # Custom authentication logic if needed
    pass

# permissions.py

from rest_framework.permissions import BasePermission

class CustomPermission(BasePermission):
    # Custom permission logic if needed
    pass
