from django.contrib.auth.models import Group
from .models import Profile
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save, sender=Profile)
def add_user_to_students_group(sender, instance, created, **kwargs):

    if created:
        try:
            # Primero me fijo si existe o el grupo 'estudiante'
            students = Group.objects.get(name = 'estudiante') # Si existe lo asigno a la var 'estudiante'
        except Group.DoesNotExist: 
            # Si el grupo estudiante no existe, lo creo con create
            students = Group.objects.create(name='estudiante')
        # Por último asigno la instancia del perfil que se acaba de crear al grupo estudiante
        instance.user.groups.add(students)
            