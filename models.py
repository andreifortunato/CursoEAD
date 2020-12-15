from django.db import models

  class Course(models.Model):

    name=models.CharField('Nome', max_length=100)
    slug=models.SlugField('Atalho')
    description=models.TextField('Descrição', blank=True)
    start_date=models.DataField('Data de Início', null=True, blank=True)
    image=models.ImageField( upload_to='courses/images', verbose_name='Image', null=True, blanck=True)
    created_at=models.DataTimeField('Criado em', auto_now_add=True)
    updated_at=models.DataTimeField('Atualizado em', auto_now=True)

