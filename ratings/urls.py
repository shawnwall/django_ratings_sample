from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView, CreateView
from models import Thing
from djangoratings.views import AddRatingFromModel
from django.core.urlresolvers import reverse

urlpatterns = patterns('ratings.views',
    url(r'^$', ListView.as_view(
        model=Thing,
        paginate_by=10
    )),
    url(r'^add/$', CreateView.as_view(
        model=Thing,
        success_url='/'
    )),
    url(r'^rate/(?P<object_id>\d+)/(?P<score>\d+)/', AddRatingFromModel(), {
        'app_label': 'ratings',
        'model': 'thing',
        'field_name': 'rating',
    }),    
)
