from django.db import models

# Owner Info
class Owner(models.Model):
    oid = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    resident_type = models.CharField(max_length=50, choices=[('owner', 'Owner'), ('tenant', 'Tenant')])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Property Info
class Property(models.Model):
    pid = models.AutoField(primary_key=True)
    address = models.TextField(unique=True)  # Ensuring unique address
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    gps_latitude = models.FloatField()  # GPS Latitude
    gps_longitude = models.FloatField()  # GPS Longitude
    rent_status = models.BooleanField(default=False)  # True for rented, False for available
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, default=1)  # Default Owner ID is 1

    def __str__(self):
        return self.address

# Feedback/Issue Remarks (for public feedback)
class Feedback(models.Model):
    fid = models.AutoField(primary_key=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    remarks = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback for {self.property.address}"
