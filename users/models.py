from django.db import models


class User(models.Model):
    login = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.login


class XrefUserRoom(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    room_id = models.ForeignKey('Room', on_delete=models.PROTECT)
