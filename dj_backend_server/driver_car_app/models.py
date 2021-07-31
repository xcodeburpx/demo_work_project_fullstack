from django.db import models


# Driver class - correlate to trucks
class Driver(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Brand - check hwo choices work
class Brand(models.Model):
    brand_name = models.CharField(
        max_length=32,
        choices=[("Volvo", "Volvo"), ("Opel", "Opel")])

    def __str__(self):
        return f"{self.brand_name}"

# Truck class - correlate GPS records with vehicle
class Truck(models.Model):
    truck_name = models.CharField(max_length=300)
    engine_size = models.DecimalField(
        max_digits=8, decimal_places=4)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f"{self.truck_name}"

# Gps class - hold Gps records in database
class Gps(models.Model):
    timestamp = models.DateTimeField()
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE, related_name="locations")
    longitude = models.DecimalField(
        max_digits=8, decimal_places=4)
    latitude = models.DecimalField(
        max_digits=8, decimal_places=4)
    altitude = models.DecimalField(
        max_digits=8, decimal_places=4)

    def __str__(self):
        return f"{self.timestamp} {self.longitude} {self.latitude} " \
               f"{self.altitude}"
