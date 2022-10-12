from django.contrib import admin
from django.urls import path, re_path, include

from enterprise.views import \
    EnterpriseAPIView, \
    EnterpriseAPIList, \
    ProductAPIList, \
    ProductAPIView, \
    CommodityAPIView,\
    CommodityAPIList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('organizations/<int:pk>/', EnterpriseAPIList.as_view()),
    path('organization/<int:pk>/', EnterpriseAPIView.as_view()),

    path('products/', ProductAPIList.as_view(), name='products'),
    path('product/<int:pk>/', ProductAPIView.as_view()),

    path('commodities/<int:pk>/', CommodityAPIList.as_view()),
    path('commodity/<int:pk>/', CommodityAPIView.as_view()),

    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

]
