from django.conf.urls import url
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    #url(r'^snippets/$', views.snippet_list),
    #url(r'^snippet/(?P<pk>[0-9]+)/$', views.snippet_detail),
    #url(r'^snippets/$',views.SnippetList.as_view()),
    #url(r'^snippet/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    #url(r'^snippets/$',views.SnippetList1.as_view()),
    #url(r'^snippet/(?P<pk>[0-9]+)/$', views.SnippetDetail1.as_view()),
    url(r'^snippets/$',views.SnippetList2.as_view(), name='snippet-list'),
    url(r'^snippet/(?P<pk>[0-9]+)/$', views.SnippetDetail2.as_view(), name='snippet-detail'),
    url(r'^users/$',views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^$', views.api_root),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight'),
]

urlpatterns = format_suffix_patterns(urlpatterns)