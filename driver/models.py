from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from mytaxi import settings
from django.shortcuts import reverse


class User(AbstractUser):
    """
    We are using Django built in user with Abstract Base user
    for designing application with requirements
    """
    pass


class Client(models.Model):
    ProccessId = models.IntegerField()
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    PhoneNumber = models.CharField(max_length=100)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.FirstName


class Driver(models.Model):
    """ Driver model """
    ProccessId = models.IntegerField()
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    CarModel = models.CharField(max_length=100)
    CarNumber = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=100)
    CreatedUserId = models.ForeignKey(User, blank=False, null=True, on_delete=models.SET_NULL)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.FirstName


class Order(models.Model):
    """
    ORDER model
    """
    REQUESTED = 'REQUESTED'
    CREATED = 'CREATED'
    ACCEPTED = 'ACCEPTED'
    FINISHED = 'FINISHED'
    DELETED = 'DELETED'
    STATUSES = (
        (REQUESTED, REQUESTED),
        (CREATED, CREATED),
        (ACCEPTED, ACCEPTED),
        (FINISHED, FINISHED),
        (DELETED, DELETED),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    pick_up_address = models.CharField(max_length=255)
    drop_off_address = models.CharField(max_length=255)
    client = models.ForeignKey(Client, null=True, blank=True, on_delete=models.DO_NOTHING,
                              related_name="trips_as_rider")
    driver = models.ForeignKey(Driver, null=True, blank=True, on_delete=models.DO_NOTHING,
                               related_name="trips_as_driver")
    status = models.CharField(
        max_length=100, choices=STATUSES, default=REQUESTED
    )

    def __str__(self):
        """
        string representation
        :return:
        """
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('trip_detail', kwargs={'trip_id': self.id})