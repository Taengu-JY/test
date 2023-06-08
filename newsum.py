import base64
from gensim.summarization.summarizer import summarize
from gensim.summarization.textcleaner import split_sentences
import collections
import textwrap
import re

with open("news.txt", 'rb') as f :
    b_f =  f.read()
    encoded_article = base64.b64encode(b_f)

with open("bnews.txt", 'wb') as new_f:
    new_f.write(encoded_article)


with open("image.jpg", 'rb') as img:
    b_img = img.read()
    encoded_img = base64.b64encode(b_img)

with open("bimg", 'wb') as new_img:
    new_img.write(encoded_img)


# base64 형태로 파일을 받았다는 가정을 위하여 원본기사와 사진을 base64 형태로 만들어줌

with open("bnews.txt", 'rb' ) as f :
    article = f.read()
    decoded_article = base64.b64decode(article)
    decoded_news = decoded_article.decode('utf-8')


# base64 로 받은 파일을 디코드 해주어 나온 바이너리 파일을 utf-8로 디코드하여 사람이 볼 수 있는 형태로 만든다.

with open("bimg" , 'rb') as img :
    image = img.read()


with open("bimg.jpg", 'wb' ) as img:
    decoded_image = base64.b64decode(image)
    img.write(decoded_image)

# 이미지를 바이너리형식으로 읽어온 후 jpg 파일로 저장


# decoded_new 요약하기
#print(summarize(decoded_news, ratio=0.4))

news_summarized = summarize(decoded_news, ratio=0.4)
#print(news_summarized)

# 키워드 추출하기.
words = re.findall(r'\w+', decoded_news)
#print(words)

#빈도수 산출
counter = collections.Counter(words)
#print(counter)

#print(counter.most_common(10))


#.jion 써서 단어들 합쳐보기([1:10]의로 합치기 쉽게 만들었음)

print("".join(words[1:10]))