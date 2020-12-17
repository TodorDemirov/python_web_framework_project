from django.db.models.signals import post_save
from django.dispatch import receiver
from python_web_framework_project.authentication.models import Profile
from django.contrib.auth import get_user_model

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, *args, **kwargs):
    if created:
        profile = Profile(
            user=instance,
            display_name=instance.username
        )
        profile.save()
