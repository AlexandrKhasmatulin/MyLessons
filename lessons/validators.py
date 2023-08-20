from rest_framework import serializers

def validator_prohibited_link(value):
    if set(value.lower().split()) != set('youtube.com'):
        raise serializers.ValidationError('Недопустимая ссылка')
