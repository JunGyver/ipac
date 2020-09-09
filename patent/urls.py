from django.urls import path
from .views import (
    ChartView,
    HistoryView,
    MainView,
    ListView,
    DetailView,
    TestView,
    KeywordSearch,
)

urlpatterns = [
    path('chart', ChartView.as_view()),
    path('history', HistoryView.as_view()),
    path('main', MainView.as_view()),
    path('test', TestView.as_view()),
    path('list', ListView.as_view()),
    path('keyword', KeywordSearch.as_view()),
    path('detail', DetailView.as_view()),
]
