from django.db import models

# Create your models here.
class Incident(models.Model):
    TYPES_CHOICES = [
        ('socialengi', "usurpation d'identité"),
        ('escroquerie', 'fraude en ligne'),
        ('chantage', 'Cyber harcèlement'),
        ('phishing', 'Hameçonnage'),
        ('malware', 'Logiciel malveillant'),
        ('hacking', 'Piratage de compte'),
    ]
    
    type_incident = models.CharField(max_length=50, choices=TYPES_CHOICES)
    description = models.TextField()
    email_contact = models.EmailField()
    capture_ecran = models.ImageField(upload_to='incidents/%Y/%m/', blank=True, null=True)
    date_signalement = models.DateTimeField(auto_now_add=True)
    traite = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.type_incident} - {self.date_signalement}"