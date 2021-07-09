
from todo.models import Todo
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from todo.serializer import CreateSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from todo.pagination import CustomPageNumberPagination
# Create your views here.


class TodoAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CreateSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'title', 'description', 'is_completed']
    search_fields = ['id', 'title', 'description', 'is_completed']
    ordering_fields = ['id', 'title', 'description', 'is_completed']

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)


class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CreateSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)
