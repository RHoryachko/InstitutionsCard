from django.urls import path
from .views import AllEstablishmentsListView, EstablishmentDetailView
from .views import CategoryEstablishmentListView, EstablishmentCommentsView
from .views import LeaveCommentView, RefreshTokenView

urlpatterns = [
    path('all-establishments/', AllEstablishmentsListView.as_view(), name='all-establishments-list'),
    path('establishment/<int:id>/', EstablishmentDetailView.as_view(), name='establishment-detail'),
    path('establishments/category/<str:category>/', CategoryEstablishmentListView.as_view(), 
                                                    name='category-establishments-list'),
    path('establishment/<int:id>/comments/', EstablishmentCommentsView.as_view(), 
                                                name='establishment-comments'),
    path('establishment/<int:id>/leave-comment/', LeaveCommentView.as_view(), 
                                                name='leave-comment'),
    path('token/refresh/', RefreshTokenView.as_view(), name='token_refresh'),
]