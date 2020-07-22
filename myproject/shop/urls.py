from django.urls import path,register_converter,re_path
from .converters import FourDigitYearConverter
from . import views
from .views import item_list

app_name='shop'

register_converter(FourDigitYearConverter,'yyyy')
urlpatterns = [
    #
    # path('', views.item_list, name='item_list'),                           # Item 목록
    # path('new/', views.item_new, name='item_new'),                         # 새 Item
    # path('<int:id>/', views.item_detail, name='item_detail'),              # Item 보기
    # re_path(r'^(?P<id>\d+)/$', views.item_detail, name='item_detail'),     # 혹은 re_path 활용
    # path('<int:id>/edit/', views.item_edit, name='item_edit'),             # Item 수정
    # path('<int:id>/delete/', views.item_delete, name='item_delete'),       # Item 삭제
    # path('<int:id>/reviews/', views.review_list, name='review_list'),      # 리뷰 목록
    # path('<int:item_id>/reviews/<int:id>/edit/$', views.review_edit, name='review_edit'),
    # path('<int:item_id>/reviews/<int:id>/delete/$', views.review_delete, name='review_delete'),
    path('items/',item_list,name='item_list'),
    path('shop/',views.item_list),
    path('archives/<yyyy:year>/',views.archives_year),
]