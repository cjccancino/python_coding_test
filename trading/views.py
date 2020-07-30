from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,CreateAPIView
from rest_framework.response import Response
from rest_framework import generics, permissions, renderers
from rest_framework import status
from .models import Stock, StockFolioUser, StockPortfolio
from .serializers import StockSerializer, StockFolioSerializer, StockPortfolioSerializer, LoginSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly



class StockListCreate(CreateAPIView):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()



class StockList(ListAPIView):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()



class StockRetrieve(RetrieveAPIView):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()



class StockRetrieveUpdate(RetrieveUpdateAPIView):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()



class StockRetrieveDelete(RetrieveDestroyAPIView):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()



class StockFolioList(generics.ListCreateAPIView):
    serializer_class = StockFolioSerializer
    queryset = StockFolioUser.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class StockFolioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StockFolioUser.objects.all()
    serializer_class = StockFolioSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]



class StockPortfolioList(generics.ListCreateAPIView):
    queryset = StockPortfolio.objects.all()
    serializer_class = StockPortfolioSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]



class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer