from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    age = models.IntegerField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Song(models.Model):
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    # So when an artiste is deleted, all the songs by that artiste is also deleted from the database.
    title = models.CharField(max_length=1000)
    date_released = models.CharField(max_length=10)
    likes = models.IntegerField()
    # variable artisite_id was conflicting with the id variable in the Artiste class

    def __str__(self):
        return f"{self.title} by {self.artiste_id.__str__()}"

    
class Lyric(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.CharField(max_length=100000)
    # variable song_id was conflicting with the id variable in the Song class

    def __str__(self):
        return f"Lyrics of {self.song_id.__str__()}"