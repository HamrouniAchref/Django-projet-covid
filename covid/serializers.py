from rest_framework import serializers
from .models import Vaccin
from .models import Vaccinateur,EffetSecondaire,Declaration,Pays,Maladie



class VaccinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccin
        fields = ('id', 'nom','paysFabrication','dateFabrication', )



class  VaccinateurSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Vaccinateur
        fields = ('id', 'nom','prenom','age','pays', 'sexe','vaccin','maladies','email')



class  EffetSecondaireSerializer(serializers.ModelSerializer):
    class Meta:
        model =  EffetSecondaire
        fields = ('id', 'description','members')        

class  DeclarationSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Declaration
        fields = ('id', 'dateSymtomes','vaccinateur','effetScondaire','vaccin')

class  PaysSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Pays
        fields = ('id', 'nom',) 


class  MaladieSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Maladie
        fields = ('id', 'description')               