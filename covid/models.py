from django.db import models

# Create your models here.
class DateDeC(models.Model):
    createdAt =models.DateTimeField(auto_now_add=True)
    updatedAt =models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Pays(models.Model):
    nom=models.CharField(max_length=60)
    def __str__(self):
        return self.nom
     
class Vaccin(DateDeC):
    nom=models.CharField(max_length=60)
    paysFabrication=models.ForeignKey(Pays, on_delete=models.CASCADE)

    dateFabrication=models.DateField()
    def __str__(self):
        return self.nom

class Maladie(DateDeC):
    description=models.CharField(max_length=300)
    def __str__(self):
        return self.description
    

class Vaccinateur(DateDeC):
    nom=models.CharField(max_length=60)
    prenom=models.CharField(max_length=60)
    age=models.IntegerField()
    pays=models.ForeignKey(Pays, on_delete=models.CASCADE)
    email=models.EmailField(unique=True)
    sexe= models.CharField(max_length=9)
    validation = models.BooleanField(default=False)

    vaccin=models.ForeignKey(Vaccin, on_delete=models.CASCADE)
    maladies = models.ManyToManyField(Maladie,null=True)    
    def __str__(self):
        return self.email

class EffetSecondaire(DateDeC):
    description=models.TextField()
    members = models.ManyToManyField(Vaccinateur, through='Declaration')
    def __str__(self):
        return self.description

class Declaration(DateDeC):
    dateSymtomes=models.DateTimeField()
    models.BooleanField(default=False)
    vaccinateur= models.ForeignKey(Vaccinateur, on_delete=models.CASCADE)
    effetScondaire = models.ForeignKey(EffetSecondaire, on_delete=models.CASCADE) 
    vaccin = models.ForeignKey(Vaccin, on_delete=models.CASCADE)
     
   