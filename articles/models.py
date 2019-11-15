from django.contrib.auth import get_user_model
from django.db import models


class Article(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    codeInsee = models.CharField(max_length=100)
    pivotLocal = models.TextField()
    nom = models.TextField()
    editeurSource = models.TextField()
    dateMiseAjour = models.DateTimeField(auto_now_add=True)
    email = models.TextField()
    codePostal = models.CharField(max_length=60)
    nomCommune = models.TextField()
    telephone = models.CharField(max_length=80)
    latitude = models.DecimalField(
        null=True,
        blank=True,
        decimal_places=15,
        max_digits=19,
        default=0
    )
    longitude = models.DecimalField(
        null=True,
        blank=True,
        decimal_places=15,
        max_digits=19,
        default=0
    )

    def __str__(self):
        return self.nom


    @property
    def location_field_indexing(self):
        """Location for indexing.

        Used in Elasticsearch indexing/tests of `geo_distance` native
        filter.
        """
        return {
            'lat': self.latitude,
            'lon': self.longitude,
        }

#    class Meta:
#        ordering = ['-id']
