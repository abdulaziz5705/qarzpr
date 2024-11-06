from django.shortcuts import render
from rest_framework import generics

from contrack.models import ContrackModel, ContrackStatus
from contrack.serializer import ContrackSerializer


class ContrackView(generics.ListCreateAPIView):
    serializer_class = ContrackSerializer
    queryset = ContrackModel.objects.all()

    def perform_create(self, serializer):
        contrack = serializer.save (
            who=self.request.user,
            status=ContrackStatus.waiting.value
        )

    def get_queryset(self):
        return ContrackModel.objects.filter(who=self.request.user).exclude(status=ContrackStatus.deleted.value)