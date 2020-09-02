from django.urls import path
from .views import ChartView, HistoryView, MainView

urlpatterns = [
    path('chart', ChartView.as_view()),
    path('history', HistoryView.as_view()),
    path('main', MainView.as_view()),
]
