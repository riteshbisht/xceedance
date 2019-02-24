from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from features.choices import FEATURE_STATUS, PRODUCT_CHOICES
# Create your models here.


class AbstractAutoDate(models.Model):
    created = models.DateTimeField(editable=False, auto_now_add=True,)
    modified = models.DateTimeField(null=True, blank=True, auto_now=True)

    class Meta:
        abstract = True


class TargetVersion(AbstractAutoDate):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = _("TargetVersion")
        verbose_name_plural = _("TargetVersions")

class Client(AbstractAutoDate):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = _("Client")
        verbose_name_plural = _("Clients")

    def __str__(self):
        return self.name

class Feature(AbstractAutoDate):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.TextField(null=True, blank=True, verbose_name=_('Description'))
    status = models.IntegerField(choices=FEATURE_STATUS, default=0)
    last_status = models.IntegerField(choices=FEATURE_STATUS, default=0)
    priority = models.PositiveIntegerField(default=0)
    target_date = models.DateField()
    client = models.ForeignKey('features.Client', related_name='client_feature')
    product = models.IntegerField(choices=PRODUCT_CHOICES,)

    class Meta:
        verbose_name = _("Feature")
        verbose_name_plural = _("Features")

    def save(self, *args, **kwargs):
        all_features = self.client.client_feature.filter(priority=self.priority).order_by('priority')
        if all_features.exists():
            features_with_higher_priorty = all_features.filter(priority__gte=self.priority)
            for feature in features_with_higher_priorty:
                feature.priority = feature.priority + 1
                feature.save()

        super(Feature, self).save(*args, **kwargs)


    def __str__(self):
        return self.title
