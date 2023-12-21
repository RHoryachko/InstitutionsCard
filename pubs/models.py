# establishments/models.py

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Establishment(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00, editable=False)
    description = models.TextField(blank=True)
    photo1 = models.ImageField(upload_to='establishment_photos/', blank=True, null=True)
    photo2 = models.ImageField(upload_to='establishment_photos/', blank=True, null=True)
    photo3 = models.ImageField(upload_to='establishment_photos/', blank=True, null=True)
    
    CATEGORY_CHOICES = [
        ('cheap', 'Дешево'),
        ('medium', 'Середньо'),
        ('expensive', 'Дорого'),
        ('very_expensive', 'Дуже дорого'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='medium')

    def __str__(self):
        return self.name



class Comment(models.Model):
    establishment = models.ForeignKey('Establishment', related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.author.username} - {self.establishment.name}"



@receiver(post_save, sender=Comment)
def update_establishment_rating(sender, instance, **kwargs):
    establishment = instance.establishment
    comments = establishment.comments.all()
    if comments:
        total_rating = sum(comment.rating for comment in comments)
        establishment.rating = total_rating / len(comments)
        establishment.save()
    else:
        establishment.rating = 0.00
        establishment.save()
