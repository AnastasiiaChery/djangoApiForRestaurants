from django.urls import path


from restApi.views import RestListCreateView, NameMenuView, RankListView, LuxListView

urlpatterns = [
    path('', RestListCreateView.as_view(),  name='show_rest'),
    path('/sorted', RankListView.as_view(),  name='sort'),
    path('/luxury', LuxListView.as_view(),  name='luxury'),
    path('/<str:dish>', NameMenuView.as_view(),  name='name_menu')
]