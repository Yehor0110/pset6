import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives="positive-words.txt", negatives="negative-words.txt"):
        """Initialize Analyzer."""
        
        self.positives = set()
        self.negatives = set()
        
        # import positives words
        file = open(positives, "r")
        for line in file:
            if(line.startswith(";")):
                continue
            self.positives.add(line.rstrip("\n"))
        file.close()
        self.positives.pop()
        
        # import negatives words
        file = open(negatives, "r")
        for line in file:
            if(line.startswith(";")):
                continue
            self.negatives.add(line.rstrip("\n"))
        file.close()
        self.negatives.pop()
        
    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        
        # division of the text to words
        wordsInText = nltk.word_tokenize(text)
        result = 0
        
        # check word from the text in lists and 
        for i in wordsInText:
            result += i.lower() in self.positives
            result -= i.lower() in self.negatives
            
        return result
