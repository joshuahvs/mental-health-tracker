from django.db import models

# Create your models here.
#models.Model adalah kelas dasar yang digunakan untuk mendefinisikan model dalam Django. MoodEntry adalah nama model yang didefinisikan.
class MoodEntry(models.Model):
    mood = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    feelings = models.TextField()
    mood_intensity = models.IntegerField()

    #menambahkan atribut read-only
    @property 
    def is_mood_strong(self):
        return self.mood_intensity > 5