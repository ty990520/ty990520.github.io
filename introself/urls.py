from django.contrib import admin
from django.urls import path
import me.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', me.views.home, name="home"),
    path('profile/', me.views.profile, name="profile"),
    path('itservice/', me.views.itservice, name="itservice"),
]
