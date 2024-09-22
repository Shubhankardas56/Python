from wordcloud import WordCloud,STOPWORDS
import sys
import numpy
from PIL import Image
import wikipedia
topic=str(input('Enter Topic: '))
searched_topic=wikipedia.search(topic)
page=wikipedia.page(searched_topic)
content=page.content
stopwords=set(STOPWORDS)
wc=WordCloud(background_color='black',max_words=200,stopwords=stopwords)
wc.generate(content)
wc.to_file("output.jpg")
print("success")


