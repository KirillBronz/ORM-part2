from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
    
    class Meta:
     verbose_name = "tag"
     verbose_name_plural = "tags"

class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    text = models.TextField(verbose_name="text")
    publish_date =  models.DateTimeField(verbose_name="date&&time of publication")
    image = models.ImageField(null=True, blank=True, verbose_name="image")
    scope = models.ManyToManyField(Topic, through='Scope')

class Meta:
    verbose_name = 'article'
    verbose_name_plural = "articles"

def __str__(self):
    return self.title 

class Scope(models.Model):
    tag = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name="selection")
    main = models.BooleanField(default=False, verbose_name='Main')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')

class Meta:
 verbose_name = "article theme"
 verbose_name_plural = "site theme"
 ordering = ['-main', 'tag_name']
