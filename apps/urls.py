from django.urls import include, path
from . import views

app_name = 'apps'

urlpatterns = [
    path("", views.index, name="index"),
    path("predictword/", views.mask1, name="mask1"),
    path('predictwordresult/', views.mask2, name='mask2'),
    path('summarization/', views.summarize1, name='summarize1'),
    path('summarizeresult/', views.summarize2, name='summarize2'),
    path('textgenerator/', views.textgenerator1, name='textgenerator1'),
    path('textgeneratorresult/', views.textgenerator2, name="textgenerator2"),
    path('questions/', views.qa1, name='qa1'),
    path('answers/', views.qa2, name='qa2'),
    path('classification/', views.sentimental1, name='sentimental1'),
    path('sentimentalanalysis/', views.sentimental2, name='sentimental2'),
    path('translation/', views.translate1, name='translate1'),
    path('translationresult/', views.translate2, name='translate2'),
]
