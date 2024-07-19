from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.

# PERFIL DE USUARIO
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')
    image = models.ImageField(default="users/usuario_defeco.jpg", upload_to="users/", verbose_name="Imagen de perfil")
    address = models.CharField(max_length= 150, null=True, blank=True, verbose_name="dirección")
    location = models.CharField(max_length=150, null=True, blank=True, verbose_name="localidad")
    telephone = models.CharField(max_length=50, null=True, blank=True, verbose_name="Teléfono")

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = "Perfiles"
        ordering = ['-id']

    def __str__(self) -> str:
        return self.user.username
    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
