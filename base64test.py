# text를 base64로 인코딩 하고 디코딩한 후 출력
import base64

with open("news.txt", "rb") as f:

    article = f.read()

    encoded_article = base64.b64encode(article)
    encoded_text = encoded_article.decode('utf-8')

    decoded_article = base64.b64decode(encoded_article)
    decoded_text = decoded_article.decode('utf-8')

    print(decoded_text)
