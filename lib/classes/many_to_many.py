class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and 5 <= len(title) <= 50 and hasattr(self, '_title') == False:
            self._title = title
        else:
            raise ValueError("Title must be a string and between 5 ane 50 characters long!")
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine

        
class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0 and hasattr(self, '_name') == False:
            self._name = name
        else:
            raise ValueError("Name must be string and be at least one character!")

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        unique_magazines = []
        for article in Article.all:
            if article.magazine not in unique_magazines and article.author == self:
                unique_magazines.append(article.magazine)
        return unique_magazines

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        unique_magazines = []
        for article in Article.all:
            if article.magazine not in unique_magazines and article.author == self:
                unique_magazines.append(article.magazine)
        if len(unique_magazines) == 0:
            return None
        else:
            unique_categories = []
            for magazine in unique_magazines:
                unique_categories.append(magazine.category)
            return unique_categories

class Magazine:

    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise ValueError('Name must be a tring and between 2 and 16 characters!')

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError('Category must be a string and has at least 1 character!')

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        unique_authors = []
        for article in Article.all:
            if article.author not in unique_authors and article.magazine == self:
                unique_authors.append(article.author)
        return unique_authors

    def article_titles(self):
        articles_ = [article.title for article in Article.all if article.magazine == self]
        if len(articles_) > 0:
            return articles_
        else:
            return None


    def contributing_authors(self):
        magazine_authors = [article.author for article in Article.all if article.magazine == self]
        if len(magazine_authors) == 0:
            return None
        else:
            cont_author = [author for author in magazine_authors if magazine_authors.count(author) > 2]
            if len(cont_author) == 0:
                return None
            else:
                return cont_author
    
    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        magazine_list = [article.magazine for article in Article.all]
        return max(set(magazine_list), key = magazine_list.count)
