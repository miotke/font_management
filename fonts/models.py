from django.db import models
from django.utils import timezone


class FontFamily(models.Model):
    """
    FontFamily will be a container for fonts.
    This will have a one-to-many relationship to fonts associated
    with the Font class.
    """

    # Font family detail
    font_family_name = models.CharField(max_length=100)
    path_to_font_family = models.CharField(max_length=100)


    def save(self):
        super().save()


    def __str__(self):
        return self.font_family_name


class Font(models.Model):

    # Individual font details
    font_name = models.CharField(max_length=100)
    font_family = models.ForeignKey(FontFamily, related_name="fonts", on_delete=models.PROTECT)
    checked_out = models.BooleanField(default=False)

    class Meta:
        ordering = ["font_family"]


    def save(self):
        super().save()


    def __str__(self):
        return f"{self.font_family} --> {self.font_name}"