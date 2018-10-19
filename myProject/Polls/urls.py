from django.urls import path
from .  import views
app_name = 'polls'
urlpatterns=[
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/',views.DetailView.as_view(),name='detail'),
    path('<int:pk>/results/',views.ResultsView.as_view(),name='results'),
    path('<int:question_id>/vote/',views.vote,name='vote'),
    path('resultsALL/', views.ResultsallView.as_view(), name='resultsall'),
    path('add/',views.questionadd,name='question-add'),
    path('<int:question_id>/addChoice/',views.choiceadd,name='choiceadd'),
    path('<int:question_id>/delete/',views.questiondelete,name='questiondelete'),
    path('<int:question_id>/edit/',views.questionedit,name='questionedit')
]
