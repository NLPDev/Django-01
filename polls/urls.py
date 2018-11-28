from django.urls import path

from . import views

app_name='polls'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('/<int:pk>/', views.DetailView.as_view(), name='detail'),
	path('/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
	path('/<int:question_id>/vote/', views.vote, name='vote'),
	path('articles/2003/', views.special_case_2003),
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<slug:slug>/', 
]
