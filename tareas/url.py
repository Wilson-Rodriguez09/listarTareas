from django.urls import path
from.views import *

urlpattern = [
    path('',listar,name='listar'),
    path('crear',crear,name='crear')
]