from rest_framework import generics
from .models import Establishment, Comment
from .serializers import EstablishmentSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .utils import valid_user
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView




class AllEstablishmentsListView(generics.ListAPIView):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer



class EstablishmentDetailView(generics.RetrieveAPIView):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer
    lookup_field = 'id'



class CategoryEstablishmentListView(generics.ListAPIView):
    serializer_class = EstablishmentSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return Establishment.objects.filter(category=category)



class EstablishmentCommentsView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        establishment_id = self.kwargs['id']
        return Comment.objects.filter(establishment__id=establishment_id)



class LeaveCommentView(generics.CreateAPIView):
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        # Отримати токен із запиту
        access_token_str = self.request.headers.get('Authorization', '').split(' ')[1]

        # Перевірити валідність та отримати користувача
        user = valid_user(access_token_str)

        if user:
            # Отримати ідентифікатор закладу з URL
            establishment_id = self.kwargs.get('id')

            try:
                # Перевірити існування закладу
                establishment = Establishment.objects.get(pk=establishment_id)
            except Establishment.DoesNotExist:
                raise Http404("Заклад не знайдено")

            # Зберегти коментар
            serializer.save(establishment=establishment, author=user)
        else:
            raise Http404("Користувач не знайдений")



class RefreshTokenView(APIView):

    def post(self, request):
        refresh_token = request.data.get('refresh_token')

        try:
            token = RefreshToken(refresh_token)
            access_token = str(token.access_token)
            return Response({'access': access_token})
        except Exception as e:
            return Response({'error': 'Invalid token or token expired.'})
