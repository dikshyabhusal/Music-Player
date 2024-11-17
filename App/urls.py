from django.conf  import settings
from django.conf.urls.static import static
from .import views
from django.urls import path

app_name = 'app'

urlpatterns = [
    path('',views.index,name="index"),
    path('song/<int:song_id>/', views.song_detail, name='song_detail'), 
]
