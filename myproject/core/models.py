from django.db import models


class Repo(models.Model):
    slug = models.BigIntegerField(
        unique=True,
        help_text='slug is id of github api'
    )
    name = models.TextField()
    full_name = models.TextField()
    html_url = models.URLField()
    stargazers_count = models.PositiveIntegerField()

    class Meta:
        ordering = ('-stargazers_count',)

    def __str__(self):
        return self.name

    def to_dict_json(self):
        return {
            'slug': self.slug,
            'name': self.name,
            'full_name': self.full_name,
            'html_url': self.html_url,
            'stargazers_count': self.stargazers_count,
        }
