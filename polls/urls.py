from django.conf.urls import url
from . import views
app_name ='polls'
urlpatterns=[
#example of polls/
url(r'^$',views.IndexView.as_view(),name='index'),
#example /polls5
url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),
#polls results
url(r'^(?P<pk>[0-9]+)/results/$',views.ResultsView.as_view(),name='results'),
#polls vote
url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),

]
