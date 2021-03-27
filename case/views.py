from case.models import Case
from rest_framework import viewsets
# from rest_framework import permissions
from case.serializers import CaseSerializer


class CaseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    # permission_classes = [permissions.IsAuthenticated]
