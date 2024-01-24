from django.db import models

# Create your models here.
CAMPUS = (('nakamozu', '中百舌鳥キャンパス'), ('sugimoto', '杉本キャンパス'), ('morinomiya', '森ノ宮キャンパス'), ('abeno', '阿倍野キャンパス'), ('habikino', '羽曳野キャンパス'), ('rinnkuu', 'りんくうキャンパス'))
class Facility(models.Model):
    name = models.CharField(max_length=100)
    eng_name = models.CharField(max_length=100, default="new facility")
    image = models.CharField(max_length=100, default="image.jpg")
    url = models.CharField(max_length=100, default="url")
    location = models.CharField(
        max_length=100,
        choices = CAMPUS
    )

    def __str__(self):
        return self.name