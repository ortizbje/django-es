from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from articles import documents as articles_documents
 
 
class ArticleDocumentSerializer(DocumentSerializer):
    class Meta:
        document = articles_documents.ArticleDocument
        fields = (
            'id',
            'codeInsee',
            'pivotLocal',
            'nom',
            'editeurSource',
            'dateMiseAjour',
            'email',
            'codePostal',
            'nomCommune',
            'latitude',
            'longitude',
            'telephone',
        )
