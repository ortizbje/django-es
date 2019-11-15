from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_RANGE,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
    LOOKUP_FILTER_GEO_DISTANCE,
    LOOKUP_FILTER_GEO_POLYGON,
    LOOKUP_FILTER_GEO_BOUNDING_BOX,
    SUGGESTER_COMPLETION,
)
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend,
    SearchFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
 
from articles import documents as articles_documents
from articles import serializers as articles_serializers

class ArticleViewSet(DocumentViewSet):
    document = articles_documents.ArticleDocument
    serializer_class = articles_serializers.ArticleDocumentSerializer
 
    lookup_field = 'id'
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]
 
    # Define search fields
    search_fields = (
        'nom',
        'pivotLocal',
        'codePostal',
        'nomCommune',
    )

    # Filter fields
    filter_fields = {
        'id': None,
        'codePostal': 'codePostal.raw',
        'pivotLocal': 'pivotLocal.raw',
        'nomCommune': 'nomCommune.raw',
        'dateMiseAJour': 'dateMiseAJour',
    }

    # Define ordering fields
    ordering_fields = {
        'id': None,
        'nomCommune': 'nomCommune.raw',
    }

    # Specify default ordering
    ordering = ('nomCommune',)

    # Define geo-spatial filtering fields
    geo_spatial_filter_fields = {
        'location': {
            'lookups': [
                LOOKUP_FILTER_GEO_BOUNDING_BOX,
                LOOKUP_FILTER_GEO_DISTANCE,
                LOOKUP_FILTER_GEO_POLYGON,

            ],
        },
    }

    # Define ordering fields
    geo_spatial_ordering_fields = {
        'location': None,
    }
