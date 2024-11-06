from rest_framework import serializers

from contrack.models import ContrackModel, ContrackType, ContrackMoney, ContrackStatus


class ContrackSerializer(serializers.ModelSerializer):
    back_money = serializers.DateTimeField(required=False)
    note = serializers.CharField(required=False, max_length=255)
    type = serializers.ChoiceField(choices=ContrackType.choices)
    currence = serializers.ChoiceField(choices=ContrackMoney.choices)


    class Meta:
        model = ContrackModel
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at', 'whom', 'status']
