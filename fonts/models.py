from django.db import models
from django.utils import timezone


class FontFamily(models.Model):
    """
    FontFamily will be a container for fonts.
    This will have a one-to-many relationship to fonts associated
    with the Font class.
    """

    # Font family detail
    font_family_creator_name = models.CharField(max_length=100, blank=True)
    # font_family_name = models.CharField(max_length=100, blank=True)
    # purchase_date = models.DateField(default=timezone.now)
    # cost = models.DecimalField(max_digits=7, decimal_places=2, blank=True)
    path_to_font_family = models.CharField(max_length=100)


    def save(self):
        super().save()


    def __str__(self):
        return self.path_to_font_family



class Font(models.Model):

    # Individual font details
    font_name = models.CharField(max_length=100)
    #font_family = models.ForeignKey(FontFamily, on_delete=models.PROTECT)
    checked_out = models.BooleanField(default=False)
    assigned_to = models.CharField(max_length=100, blank=True)


    def save(self):
        super().save()


    def __str__(self):
        return str([str(self.font_family), str(self.font_name)])


    # class Meta:
    #     ordering = ["font_family"]
