# models

from django.db import models
from django.contrib.auth.models import User

class Bedrijven(models.Model):

    bedrijfsnaam = models.CharField(max_length = 50)

    def __str__(self):
        return str(self.bedrijfsnaam)

    class Meta:
        verbose_name_plural = "Bedrijven"

class Projecten(models.Model):

    projectnummer = models.CharField(max_length = 10)
    projectnaam = models.CharField(max_length = 30)
    plaats = models.CharField(max_length = 20)

    def __str__(self):
        return str(self.projectnummer) + ' | ' + self.projectnaam


class Vloeren(models.Model):

    nummer = models.CharField(max_length = 10)
    documentnaam = models.CharField(max_length = 50)
    #afbeelding_document = models.ImageField(upload_to='afbeelding_documenten/', blank=True)
    bestand = models.FileField(upload_to = 'documenten/', blank=True, null=True)
    bedrijfsnaam = models.ForeignKey(Bedrijven, on_delete=models.CASCADE)
    projectnaam = models.ForeignKey(Projecten, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.nummer) + ' | ' + self.documentnaam

#    def laatste_datum(self):
#        alle_datums = self.datum.all()
#        laatste_datum = datum.latest('datum')
#        return laatste_datum

    class Meta:
        verbose_name_plural = "Vloeren"

class Datum_Document(models.Model):

    datum = models.DateField()
    vloeren = models.ForeignKey(Vloeren, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.datum)


class Controlemomenten_gepland(models.Model):

    ter_eerste_controle_gepland = models.DateField()
    ter_eerste_controle_retour_binnen_gepland = models.DateField()
    ter_tweede_controle_gepland = models.DateField()
    ter_tweede_controle_retour_binnen_gepland = models.DateField()
    definitief_binnen_gepland = models.DateField()
    datum = models.ForeignKey(Datum_Document, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Geplande controlemomenten"


