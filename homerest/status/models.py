from django.db import models
from django.conf import settings

# 
def upload_status_image(instance,filename):
    return "status/{user}/{filename}".format(user=instance.user,filename=filename)

# 
class StatusQuerySet(models.QuerySet):
    pass

#
class StatusManager(models.Manager):
    def get_queryset(self):
        return StatusQuerySet(self.model,using=self._db)

class Status(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    context = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to=upload_status_image,null=True,blank=True) 
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    #
    objects = StatusManager()

    def __str__(self):
        return str(self.user.username)

    class Meta:
        verbose_name = "Status post"
        verbose_name_plural = "Status posts"

    # link our user column attribute of status object to be called as owner
    @property
    def owner(self):
        return self.user