from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from application.models import Profile
from application.models import JobSeeker, Company

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=User)
def create_jobseeker(sender, instance, created, **kwargs):
    if created:
        JobSeeker.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_company(sender, instance, created, **kwargs):
    if created:
        Company.objects.create(user=instance)