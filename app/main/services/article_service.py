from ..models import Article
class ArticleService:
    def get_new_article(self):
        article = Article()
        article.id = 1
        article.title = 'Title 1'
        article.description = 'Description'
        return article
    
    def get_articles(self):
        articles = []
        article = Article()
        article.id = 1
        article.title = 'Title 1'
        article.description = 'Description'
        articles.append(article)
        article = Article()
        article.id = 2
        article.title = 'Title 2'
        article.description = 'Description 2'
        articles.append(article)
        return articles

