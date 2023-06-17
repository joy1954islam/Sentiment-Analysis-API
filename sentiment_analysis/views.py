from rest_framework.views import APIView
from rest_framework.response import Response
from transformers import pipeline


class SentimentAnalysisView(APIView):
    def post(self, request):
        try:
            text = request.data.get('text')
            if not text:
                return Response({'error': 'Text not provided.'}, status=400)
            sentiment_classifier = pipeline("sentiment-analysis")
            result = sentiment_classifier(text)[0]
            sentiment = result['label']
            sentiment_score = result['score']
            response_data = {
                'sentiment': sentiment,
            }
            return Response(response_data)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
