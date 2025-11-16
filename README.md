# TEXT-SUMMARIZATION-TOOL

*COMPANY* : CODTECH IT SOLUTIONS

*NAME* : LEONA MENDES

*INTERN ID* : CT04DR1252

*DOMAIN NAME* : ARTIFICIAL INTELLIGENCE

*DURATION* : 4 WEEKS 

*MENTOR* : NEELA SANTOSH


# TASK 1 — TEXT SUMMARIZATION 

Text summarization is an essential Natural Language Processing (NLP) task designed to reduce long pieces of text into shorter, meaningful summaries without losing important information. In this task, the objective was to build an automatic summarization system that can take long paragraphs or articles and generate concise, readable summaries. To achieve this, I implemented a summarizer using the **Hugging Face Transformers library**, specifically the **BART (facebook/bart-large-cnn)** model, which is widely used for high-quality abstractive summarization. The goal was to demonstrate how modern AI can understand, interpret, and condense language in a human-like manner.

The summarization method used here is **abstractive summarization**, which means the model does not copy or extract exact sentences from the original text. Instead, it rewrites the content in its own words while preserving the key ideas. This is similar to how humans summarize: by understanding the meaning first and then expressing it in a shorter form. The BART model is well-suited for this because it is a transformer-based encoder–decoder architecture trained on huge text datasets, making it capable of understanding context, relationships, and meaning at a deep level.

The code implementation starts by importing the summarization pipeline from the Transformers library. Pipelines make it simple to use complex models with just one or two lines of code. The model `"facebook/bart-large-cnn"` is then loaded, which comes pre-trained and fine-tuned specifically for summarization tasks. For testing, I used an example paragraph from the show *Stranger Things*, but the script is flexible enough to summarize any input text provided by the user. The summarization function is then called with parameters like `max_length` and `min_length`, which help control how long the summary should be. Finally, the script prints both the original text and the generated summary to show the effectiveness of the model.

This task demonstrates a very practical application of NLP. In the real world, text summarization is used in many industries. In journalism, reporters can quickly summarize long articles, interviews, or reports. In education, students and researchers can summarize chapters, articles, or academic papers to save time while studying. In customer-service sectors, companies can summarize long complaint emails or large sets of customer feedback. In business and law, professionals can condense lengthy documents, contracts, and reports into shorter, easier-to-read versions. Even in entertainment and content creation, summarization helps creators turn long scripts or stories into short descriptions. With the explosion of digital text, summarization has become a highly valuable tool for saving time and improving productivity.

Overall, Task 1 successfully shows how AI can make text processing more efficient. Using BART through the Hugging Face pipeline allowed the creation of a summarization system that is both powerful and easy to implement. With only a few lines of code, the model can understand and rewrite complex text in a shorter, clearer format. This task not only demonstrates technical understanding of NLP but also highlights how AI can be applied to everyday tasks that require quick understanding of long information. It shows how summarization models are becoming essential tools in modern workflows where time, clarity, and efficiency matter.


