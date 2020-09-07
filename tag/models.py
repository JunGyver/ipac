from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50)
    count = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'categories'


class Tag(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    count = models.CharField(max_length=100)
    tagmaster = models.ManyToManyField('patent.Master', through='TagMaster', related_name='tagging')

    class Meta:
        db_table = 'tags'

class TagMaster(models.Model):
    tag = models.ForeignKey('Tag', on_delete=models.SET_NULL, null=True, related_name='tags')
    master =models.ForeignKey('patent.Master', on_delete=models.SET_NULL, null=True, related_name = 'masters')

    class Meta:
        db_table = 'tags_masters'

