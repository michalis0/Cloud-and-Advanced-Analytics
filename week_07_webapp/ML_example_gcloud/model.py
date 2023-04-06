import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
#from textblob import TextBlob

class SentimentClassifierBert:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
        self.model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english", num_labels=2)
        self.model.to(self.device)

    def classify(self, text):

        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        inputs = {k: v.to(self.device) for k, v in inputs.items()}
        with torch.no_grad():
            outputs = self.model(**inputs)
        probs = torch.softmax(outputs.logits, dim=-1).tolist()[0]
        sentiment = "positive" if probs[1] > probs[0] else "negative"
        return sentiment


"""
class SentimentClassifierBlob:
    def classify(self, text):
        analysis = TextBlob(text)
        sentiment = "positive" if analysis.sentiment.polarity > 0 else "negative" if analysis.sentiment.polarity < 0 else "neutral"
        return sentiment

"""
