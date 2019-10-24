from django.db import models
from django.contrib.auth.models import User
from book.models import Contacts



class call_logs(models.Model):

    callTime = models.DateTimeField(verbose_name='Çağrı Zamanı')
    fromNumber = models.CharField(max_length=16, verbose_name='Arayan')
    toUser  = models.OneToOneField(User.get_full_name, on_delete=models.models.SET_NULL, null=True, related_name='rn_to_user')
    talkingDurations = models.DateTimeField(verbose_name='Görüşme Süresi')
    note = models.TextField(verbose_name='Not')
    id_contacts = models.ForeignKey(Contacts, on_delete=models.SET_NULL, null= True, related_name='rn_id_contacts')


