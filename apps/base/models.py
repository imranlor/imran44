from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='название сайта'
    )
    description = models.CharField(
        max_length=255,
        verbose_name='описание'
    )
    image = models.ImageField(
        upload_to='image_logo/',
        verbose_name="лого"
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'название сайта'
        verbose_name_plural = 'название сайта'

class Skils(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='название'
    )
    percent = models.CharField(
        max_length=255,
        verbose_name='процент знании'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'скил'
        verbose_name_plural = 'скилы'

class Services(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='название услуги'
    
    )
    description = models.CharField(
        max_length=400,
        verbose_name='описание'
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'услуга'
        verbose_name_plural = 'услуги'

class Projects(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='название'
    )
    description = models.CharField(
        max_length=500,
        verbose_name='описание'
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'почетная доска'
        verbose_name_plural = 'почетная доска'

class Rewievs(models.Model):
    description = models.CharField(
        max_length=500,
        verbose_name='описание'
    )
    name = models.CharField(
        max_length=255,
        verbose_name='имя'
        
    )
    profession = models.CharField(
        max_length=255,
        verbose_name='профессия'
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name='фото'
    )

    def __str__(self):
        return f"{self.description} - {self.name}"
    
    class Meta:
        verbose_name = 'Отзыв клиента'
        verbose_name_plural = 'Отзывы клиентов'

class Contacts(models.Model):
    email = models.EmailField(
        max_length=255,
        verbose_name='почта'
    )
    phone = models.CharField(
        max_length=255,
        verbose_name='ТЕЛЕФОН НОМЕР'
    )
    facebook = models.URLField(
        verbose_name='ссылка от facebook'
    )
    instagram = models.URLField(
        verbose_name='ссылка от instagram'
    )
    telegram = models.URLField(
        verbose_name='ссылка от telegram'
    )
    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Portfolio(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='имя',
        
    )
    

    image = models.ImageField(
        upload_to='image/',
        verbose_name='фото1'
    )
    image2 = models.ImageField(
        upload_to='image2/',
        verbose_name='фото2'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'фото портфолио'
        verbose_name_plural = 'фото портфолио'