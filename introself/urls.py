from django.contrib import admin
from django.urls import path
import me.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', me.views.index, name="index"),
    path('profile/', me.views.profile, name="profile"),
    path('itservice/', me.views.itservice, name="itservice"),
]
