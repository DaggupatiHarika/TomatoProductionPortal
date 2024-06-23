# market/urls.py
from django.urls import path
from .views import MarketListView, market_map, market_graph

urlpatterns = [
    path('market-list/', MarketListView.as_view(), name='market-list'),
    path('market-map/', market_map, name='market-map'),
    path('graph/<int:pk>/', market_graph, name='market-graph'),
]
