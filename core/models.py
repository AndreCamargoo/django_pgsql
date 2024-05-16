import uuid
from django.db import models
from stdimage.models import StdImageField


def get_file_path(_intance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    created_at = models.DateTimeField('Criação', auto_now_add=True)
    updated_at = models.DateTimeField('Atualização', auto_now=True)
    status = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Service(Base):
    # TUPLAS
    ICON_CHOICES = (
        ('lni-cog', 'Gear'),
        ('lni-stats-up', 'Graphic'),
        ('lni-users', 'Users'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Rock'),
    )

    service = models.CharField('title', max_length=100)
    description = models.CharField('description', max_length=200)
    icon = models.CharField('icon', max_length=20, choices=ICON_CHOICES)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.service


class Job(Base):
    job = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'

    def __str__(self):
        return self.job


class Team(Base):
    name = models.CharField('name', max_length=100)
    job = models.ForeignKey('core.Job', verbose_name='Job', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    image = StdImageField('Image', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        return self.name


class Feature(Base):
    ICON_CHOICES = (
        ('lni-rocket', 'Rocket'),
        ('lni-laptop-phone', 'Laptop-phone'),
        ('lni-cog', 'Gear'),
        ('lni-leaf', 'Leaf'),
        ('lni-layers', 'Layers')
    )
    name = models.CharField('name', max_length=100)
    description = models.TextField('description', max_length=200)
    icon = models.CharField('icon', max_length=20, choices=ICON_CHOICES)

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'

    def __str__(self):
        return self.name
