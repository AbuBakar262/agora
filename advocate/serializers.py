from rest_framework import serializers
from advocate.models import Advocate, Company


class CreateAdvocateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advocate
        fields = '__all__'


class ListAdvocateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advocate
        fields = ['id', 'name', 'profile_pic', 'short_bio', 'long_bio', 'advocate_years_exp']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        advocate_company = Company.objects.get(id=instance.company_id)
        data['company'] = {
            'id': advocate_company.id,
            'name': advocate_company.name,
            'logo': advocate_company.logo.url,
            'href': "/companies/6",
        }
        data['link'] = {
            'youtube': instance.youtube,
            'twitter': instance.twitter,
            'github': instance.github
        }
        return data


class CreateCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class ListCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'logo', 'summary']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['advocates'] = Advocate.objects.filter(company_id=instance.id).values('id', 'name', 'profile_pic', 'short_bio')
        return data