
from transformers import pipeline

# Load the summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Example long text input
text = """
Stranger Things is a 1980s-set supernatural mystery series about a group of friends in Hawkins, Indiana, who get entangled in supernatural events and government conspiracies after a young boy, Will Byers, disappears. The search for Will leads them to discover a psychokinetic girl named Eleven, who helps them and reveals the existence of an alternate dimension known as the "Upside Down". The story weaves together elements of horror, sci-fi, and drama as they battle monsters and other threats from the Upside Down, often paying homage to classic 1980s films. 
"""

# Summarize the text
summary = summarizer(text, max_length=80, min_length=30, do_sample=False)

# Print results
print("Original Text:\n", text)
print("\nSummarized Text:\n", summary[0]['summary_text'])
