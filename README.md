# Sentiment-Analysis-of-Flipkart-Review-using-NLP

Sentiment analysis, also known as opinion mining, is a subfield of Natural Language Processing (NLP) focused on identifying and categorizing opinions expressed
in text to determine the writer's attitude towards a particular topic, product, or event. This process involves analyzing text to classify it as positive, negative, or neutral.

I used publicly available data from Kaggle for the "Flipkart product review" project. The dataset can be found here: https://www.kaggle.com/datasets/harishedison/flipkart-reviews-sentiment-analysis. 
It contains product type, review, and rating information. 24% of people gave a 4-star rating. An initial analysis based on the ratings revealed that 60% of the people gave a 5-star review, while 24% gave a 4-star review. However, 7.99% gave a 1-star review, followed by a 3-star review from 6.08% of the people, and only 2% gave a 2-star review.
After the primary analysis, the dataset was cleaned to conduct sentiment analysis using the NLTK and re libraries. To categorize each text as positive, negative, or neutral, I used the Vader Lexicon library, which is explained below:
Vader Lexicon: It evaluates the given reviews and presents a matrix indicating whether the given text is positive, negative, neutral, or compound. The compound is a single-digit value that represents whether the text is positive, negative, or neutral, as shown below:

If compound score>= 0.05  then it is positive sentiment
If compound score is  <= -0.05  then it is a negative sentiment
If compound score is between  >-0.05 and <0.05 then it is neutral. 

The final analysis found that 85% of the reviews are positive, followed by 8.29% negative reviews, with only 6.73% being neutral.
