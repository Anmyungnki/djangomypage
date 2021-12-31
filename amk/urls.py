from django.urls import path #
from . import views   #


#-------------------------------------------------------------
app_name='amk'
urlpatterns = [
    path('', views.index, name='index'),  #    /amk/  , veiw.index 실행  ,  url alias index
    path('about', views.about, name='about'),  #/amk/intro/ , view.intro , url alias index     이면  디테일호출
    path('contact', views.contact, name='contact'),
    path('post', views.post, name='post'),
    path('storege', views.storege, name='storege'),
    path('storege_detail',views.storege_detail, name='storege_detail'),
#    path('<int:question_id>/results/', views.results, name='results'),        #/amk/5/results   이면  veiws.results 호출
#    path('<int:question_id>/vote/', views.vote, name='vote'),#/amk/5/vote   이면  veiws.vote 호출
  ]