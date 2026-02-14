from django.db import models
from django.utils.text import slugify


# Create your models here.
class CyberHygiene(models.Model):
    CATEGORIE_CHOICES = [
        ('deepfake', 'Deepfake'),
        ('ranconware', 'Ransonware'),
        ('phishing', 'Phishing'),
        ('fake-news', 'Fake News'),
        ('autre', 'Autre'),
    ]
  
    titre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    categorie= models.CharField(max_length=50,choices=CATEGORIE_CHOICES)
    image = models.ImageField(upload_to='cyber_hygiene/')
    description = models.TextField(max_length=700)
    date_pub =models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Conseil Cyber"
        verbose_name_plural = "Conseils Cyber"
        ordering = ['-date_pub'] # Les plus récents apparaissent en premier

    def save(self, *args, **kwargs):
        # Génère automatiquement le slug si il n'existe pas encore
        if not self.slug:
            self.slug = slugify(self.titre)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.titre} - {self.get_categorie_display()}"