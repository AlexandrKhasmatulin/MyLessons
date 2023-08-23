from rest_framework import serializers

def validator_prohibited_link(value):
    if value.lower() not in 'youtube.com':
        raise serializers.ValidationError('Недопустимая ссылка')
