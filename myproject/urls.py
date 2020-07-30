from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from trading import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^stocks/$',views.StockList.as_view()),
    url(r'^stocks/create$',views.StockListCreate.as_view()),
    url(r'^stocks/(?P<pk>[0-9]+)/$',views.StockRetrieve.as_view()),
    url(r'^stocks/(?P<pk>[0-9]+)/edit$',views.StockRetrieveUpdate.as_view()),
    url(r'^stocks/(?P<pk>[0-9]+)/delete$',views.StockRetrieveDelete.as_view()),
    url(r'^stocksfolio/$',views.StockFolioList.as_view()),
    url(r'^stocksfolio/(?P<pk>[0-9]+)/$',views.StockFolioDetail.as_view()),
    url(r'^stocksportfolio/$',views.StockPortfolioList.as_view()),
    url(r'users/', views.UserList.as_view()),
    url(r'users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]


urlpatterns += [
    url(r'api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)