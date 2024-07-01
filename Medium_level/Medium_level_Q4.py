# views.py
from django.shortcuts import render
from textblob import TextBlob

def sentiment_analysis(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        if sentiment > 0:
            sentiment_label = 'Positive'
        elif sentiment < 0:
            sentiment_label = 'Negative'
        else:
            sentiment_label = 'Neutral'
        context = {
            'text': text,
            'sentiment': sentiment_label,
            'score': sentiment
        }
        return render(request, 'sentiment_analysis.html', context)
    return render(request, 'sentiment_analysis.html')

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.sentiment_analysis, name='sentiment_analysis'),
]

# sentiment_analysis.html
<!DOCTYPE html>
<html>
<head>
    <title>Sentiment Analysis</title>
</head>
<body>
    <h1>Sentiment Analysis</h1>
    <form method="post">
        {% csrf_token %}
        <label for="text">Enter text:</label>
        <textarea name="text" id="text" rows="5"></textarea>
        <br>
        <button type="submit">Analyze Sentiment</button>
    </form>
    {% if text %}
        <h2>Sentiment Analysis Result</h2>
        <p>Text: {{ text }}</p>
        <p>Sentiment: {{ sentiment }}</p>
        <p>Sentiment Score: {{ score }}</p>
    {% endif %}
</body>
</html>