from django.urls import include, path
from . import views

app_name = 'apps'

urlpatterns = [
    path("", views.index, name="index"),
    path('summarization/', views.summarize, name='summarize'),
    path('textgenerator/', views.textgenerator, name='textgenerator'),
    path('questions/', views.qa, name='qa'),
    path('classification/', views.sentimental, name='sentimental'),
    path('translation/', views.translate, name='translate'),
]
