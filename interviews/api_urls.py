from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import InterviewViewSet, InterviewSessionViewSet, CodingChallengeViewSet, ChallengeSubmissionViewSet

router = DefaultRouter()
router.register(r'interviews', InterviewViewSet, basename='api-interview')
router.register(r'sessions', InterviewSessionViewSet, basename='api-session')
router.register(r'challenges', CodingChallengeViewSet, basename='api-challenge')
router.register(r'submissions', ChallengeSubmissionViewSet, basename='api-submission')

urlpatterns = [
    path('', include(router.urls)),
]
