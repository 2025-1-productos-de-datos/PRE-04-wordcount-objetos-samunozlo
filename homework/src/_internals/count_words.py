class CountWordsMixin:
    def count_words(self):
        """Count occurrences of each word using a plain dictionary."""
        wc = {}
        for word in self.words:
            wc[word] = wc.get(word, 0) + 1
        self.word_counts = wc