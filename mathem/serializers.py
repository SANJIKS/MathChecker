from rest_framework import serializers

class FormulaSerializer(serializers.Serializer):
    string = serializers.CharField()