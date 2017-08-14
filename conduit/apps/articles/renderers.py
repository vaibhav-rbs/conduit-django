from conduit.apps.core.renderers import ConduitJSONRenderer

class ArticleJSONRenderer(ConduitJSONRenderer):
    pagination_object_label = 'article'
    pagination_label_count = 'articlesCount'

class CommentJSONRenderer(ConduitJSONRenderer):
    pagination_object_label = 'comment'
    pagination_count_label = 'commentsCount'   