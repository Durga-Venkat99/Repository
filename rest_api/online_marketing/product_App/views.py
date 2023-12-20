# from django.shortcuts import render
# from rest_framework import generics, permissions
# from .models import Product
# from .serializers import ProductSerializer

# class ProductList(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [permissions.IsAuthenticated]







from django.shortcuts import render

def index(request):
    return render(request,'core/index.html')