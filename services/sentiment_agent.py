from textblob import TextBlob

class SentimentAgent:

    def analyze(self, headlines):

        scores = []

        for headline in headlines:

            score = TextBlob(headline).sentiment.polarity

            scores.append(score)

        if not scores:
            return 0

        return sum(scores) / len(scores)
