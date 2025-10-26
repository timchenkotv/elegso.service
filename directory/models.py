from django.db import models

class CounterpartyType(models.TextChoices):
    LEGAL = 'LEGAL', 'Юрлицо'
    PERSON = 'PERSON', 'Физлицо'
    IE = 'IE', 'ИП'
    SELFEMP = 'SELFEMP', 'Самозанятый'
    BANK = 'BANK', 'Банк'

class CountryProfile(models.TextChoices):
    RU='RU','Russia'
    US='US','USA'
    UK='UK','United Kingdom'
    EU='EU','European Union'
    DE='DE','Germany'
    FR='FR','France'
    IN='IN','India'
    CN='CN','China'
    NG='NG','Nigeria'

class CounterpartyStatus(models.TextChoices):
    ACTIVE='ACTIVE','ACTIVE'
    INACTIVE='INACTIVE','INACTIVE'
    SUSPENDED='SUSPENDED','SUSPENDED'
    MERGED='MERGED','MERGED'
    LIQUIDATED='LIQUIDATED','LIQUIDATED'

class Counterparty(models.Model):
    counterparty_id = models.BigAutoField(primary_key=True)

    type = models.CharField(max_length=16, choices=CounterpartyType.choices)
    country_profile = models.CharField(max_length=8, choices=CountryProfile.choices)
    status = models.CharField(max_length=16, choices=CounterpartyStatus.choices, default=CounterpartyStatus.ACTIVE)

    display_name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255, blank=True, null=True)
    legal_name = models.CharField(max_length=255, blank=True, null=True)

    code = models.CharField(max_length=10, unique=True, blank=True, null=True)

    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['counterparty_id']

    def __str__(self):
        return self.display_name
