from django.conf.urls import url,include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers

#for viewsets and explicit routing
#snippet_list3 = views.SnippetViewSet.as_view({
#    'get':'list',
#    'post':'create'
#    })
#snippet_detail3 = views.SnippetViewSet.as_view({
#    'get': 'retrieve',
#    'put': 'update',
#    'patch': 'partial_update',
#    'delete': 'destroy'
#})
#snippet_highlight2 = views.SnippetViewSet.as_view({
#    'get': 'highlight'
#}, renderer_classes=[renderers.StaticHTMLRenderer])
#user_list2 = views.UserViewSet.as_view({
#    'get': 'list'
#})
#user_detail2 = views.UserViewSet.as_view({
#    'get': 'retrieve'
#})




#urlpatterns = [
    #url(r'^snippets/$', views.snippet_list),
    #url(r'^snippet/(?P<pk>[0-9]+)/$', views.snippet_detail),

    #url(r'^snippets/$',views.SnippetList.as_view()),
    #url(r'^snippet/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),

    #url(r'^snippets/$',views.SnippetList1.as_view()),
    #url(r'^snippet/(?P<pk>[0-9]+)/$', views.SnippetDetail1.as_view()),
    
    #url(r'^snippets/$',views.SnippetList2.as_view(), name='snippet-list'),
    #url(r'^snippet/(?P<pk>[0-9]+)/$', views.SnippetDetail2.as_view(), name='snippet-detail'),
    #url(r'^users/$',views.UserList.as_view(), name='user-list'),
    #url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    #url(r'^$', views.api_root),
    #url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight'),
   
#    url(r'^snippets/$',snippet_list3, name='snippet-list'),
#    url(r'^snippet/(?P<pk>[0-9]+)/$', snippet_detail3, name='snippet-detail'),
#    url(r'^users/$', user_list2, name='user-list'),
#    url(r'^users/(?P<pk>[0-9]+)/$', user_detail2, name='user-detail'),
#    url(r'^$', views.api_root),
#    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', snippet_highlight2, name='snippet-highlight'),
#]

#urlpatterns = format_suffix_patterns(urlpatterns)

# Including implicit routing

from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# no need of format suffixes
#urlpatterns = format_suffix_patterns(urlpatterns)