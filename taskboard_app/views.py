from rest_framework.viewsets import ModelViewSet

from taskboard_app.models import Task
from taskboard_app.serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()