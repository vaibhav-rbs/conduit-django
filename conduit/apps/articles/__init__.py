from django.apps import AppConfig

class ArticlesAppConfig(AppConfig):
    name = 'conduit.apps.articles'
    label = 'articles'
    verbose_name = 'Articles'

    def ready(self):
        import conduit.apps.articles.signals

defualt_app_config = 'conduit.apps.articles.ArticleAppConfig'