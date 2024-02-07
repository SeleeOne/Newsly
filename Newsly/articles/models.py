from django.db import models


class Articles(models.Model):
    title = models.CharField('Title', max_length=100)
    introduction = models.CharField('Introduction', max_length=300)
    article_copy = models.TextField('Copy')
    cover_img = models.ImageField(upload_to='articles/covers', null=True, blank=True)
    date = models.DateTimeField('Publishing date')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/article/{self.id}'

    class Meta:
        verbose_name = 'Articles'