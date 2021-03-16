from django.db import models

class Days(models.TextChoices):
    Sunday="U"
    Monday="M"
    Tuesday="T"
    Wednesday="W"
    Thursday="R"
    Friday="F"
    Saturday="S"

class Sections(models.TextChoices):
    A="A"
    B="B"
    C="C"
    D="D"
    E="E"
    F="F"
    G="G"

class Ticket(models.Model):
    dateTime = models.DateTimeField()
    section = models.CharField(max_length=1, choices=Sections.choices, default=Sections.A)
    dayOfWeek = models.CharField(max_length=1, choices=Days.choices, default=Days.Monday)


