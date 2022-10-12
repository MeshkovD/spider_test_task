from django_filters import rest_framework as filters
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser

from .models import Enterprise, District, Product, Commodity
from .serializers import EnterpriseSerializer, ProductSerializer, CommoditySerializer


class EnterpriseAPIView(generics.RetrieveAPIView):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer
    permission_classes = (IsAdminUser,)
    authentication_classes = (TokenAuthentication,)


class ProductAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminUser,)
    authentication_classes = (TokenAuthentication,)


class ProductAPIList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminUser,)
    authentication_classes = (TokenAuthentication,)


class CommodityAPIView(generics.RetrieveAPIView):
    queryset = Commodity.objects.all()
    serializer_class = CommoditySerializer
    permission_classes = (IsAdminUser,)
    authentication_classes = (TokenAuthentication,)


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class EnterpriseFilter(filters.FilterSet):
    price = filters.RangeFilter(field_name='commodities__price')
    category = CharFilterInFilter(field_name='commodities__product__category__title', lookup_expr='in')

    class Meta:
        model = Enterprise
        fields = ['commodities']


class EnterpriseAPIList(generics.ListAPIView):
    serializer_class = EnterpriseSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = EnterpriseFilter
    permission_classes = (IsAdminUser,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        district_id = self.kwargs['pk']
        district = get_object_or_404(District, id=district_id)
        queryset = district.enterprise_set.all()

        if isinstance(queryset, QuerySet):
            queryset = queryset.all()
            return queryset


class CommodityAPIList(generics.ListCreateAPIView):
    serializer_class = CommoditySerializer
    permission_classes = (IsAdminUser,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        enterprise_id = self.kwargs['pk']
        enterprise = get_object_or_404(Enterprise, id=enterprise_id)
        queryset = enterprise.commodities.all()

        if isinstance(queryset, QuerySet):
            queryset = queryset.all()
            return queryset
