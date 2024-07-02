from django.db import models
from django.template.defaultfilters import slugify
from django.contrib import messages


class Location(models.Model):
    slug = models.SlugField(max_length=40)
    region = models.CharField("Region:", max_length=20)
    province = models.CharField("Province:", max_length=20)
    district = models.CharField("District:", max_length=20)
    village = models.CharField("Village:", max_length=30)
    doc = models.DateTimeField("Create Date:", auto_now_add=True)
    dou = models.DateTimeField("Update Date:", auto_now=True)

    def __str__(self):
        return f"{self.province} - {self.district}"

    # auto generate the slug
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.province}")

        while Location.objects.filter(slug=self.slug).exists():
            self.slug = slugify(f"{self.province}-{uuid.uuid4().hex[:8]}")

        messages.info(request, "Location Added Successfully.")
        super(Location, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"
