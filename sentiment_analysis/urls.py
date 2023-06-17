# sentiment_analysis_api/urls.py
from django.urls import path
from sentiment_analysis.views import SentimentAnalysisView

urlpatterns = [
    path('analyze/', SentimentAnalysisView.as_view(), name='analyze_sentiment'),
]
