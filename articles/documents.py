from elasticsearch_dsl import analyzer

from django_elasticsearch_dsl import DocType, Index, fields 

from articles import models as articles_models

article_index = Index('articles')
article_index.settings(
    number_of_shards=1,
    number_of_replicas=0
)

html_strip = analyzer(
    'html_strip',
    tokenizer="standard",
    filter=["standard", "lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)

@article_index.doc_type
class ArticleDocument(DocType):
    """Article elasticsearch document"""

    id = fields.StringField(attr='id')
    codeInsee = fields.StringField(attr='codeInsee')
    pivotLocal = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )
    nom = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )
    editeurSource = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )
    dateMiseAjour = fields.DateField()
    nomCommune = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )  
    codePostal = fields.StringField(
        analyzer=html_strip,
        fields={
            'raw': fields.StringField(analyzer='keyword'),
        }
    )
    telephone = fields.StringField(
        analyzer=html_strip,
        fields={
            'raw': fields.StringField(analyzer='keyword'),
        }
    )
    email = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )
    location = fields.GeoPointField(attr='location_field_indexing')

    class Meta:
        model = articles_models.Article
