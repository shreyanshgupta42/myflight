from django.db import models

# Create your models here.
class Airport(models.Model):
    """docstring forAirport."""
    code=models.CharField(max_length=3)
    city=models.CharField(max_length=64)

    def __str__(self):
        return f"{self.code} - {self.city}"

class Flight(models.Model):
    """docstring forFlights."""
    origin=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name='departures')
    destination=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name='arrivals')
    duration=models.IntegerField()

    def __str__(self):
        return f"{self.id}-{self.origin} to {self.destination}"

    def is_valid_flight(self):
        return (self.origin!=self.destination) and (self.duration>0)

    # Add a method that raises "Validation errors" if the data is illogical.
    def clean(self):
        if(self.origin==self.destination):
            raise ValidationError("origin and destination must be same")
        elif(duration<1):
            raise ValidationError("duration cannot be less than 1")

    """def save(self, *args, **kwargs):
        self.clean()
        # This syntax now calls Django's own "save" function, adding this data to the DB (if `clean` was ok).
        super().save(*args, **kwargs)"""

class Passenger(models.Model):
    """docstring forPassengers."""
    first=models.CharField(max_length=64)
    last=models.CharField(max_length=64)
    flights=models.ManyToManyField(Flight,blank=True,related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"
