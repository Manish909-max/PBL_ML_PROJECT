from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone
from .models import Interview, Question, InterviewSession, CandidateResponse, CodingChallenge, ChallengeSubmission
from .serializers import (
    InterviewSerializer, QuestionSerializer, InterviewSessionSerializer,
    CandidateResponseSerializer, CodingChallengeSerializer, ChallengeSubmissionSerializer
)

class InterviewViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List and retrieve active interviews.
    """
    queryset = Interview.objects.filter(status='active')
    serializer_class = InterviewSerializer
    permission_classes = [permissions.IsAuthenticated]

class InterviewSessionViewSet(viewsets.ModelViewSet):
    """
    Manage interview sessions for the authenticated user.
    """
    serializer_class = InterviewSessionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return InterviewSession.objects.filter(candidate=self.request.user)

    def perform_create(self, serializer):
        serializer.save(candidate=self.request.user)

    @action(detail=True, methods=['post'])
    def start(self, request, pk=None):
        session = self.get_object()
        if session.status != 'not_started':
            return Response({'detail': 'Session has already been started or completed.'}, status=status.HTTP_400_BAD_REQUEST)
        session.start()
        return Response({'status': 'Session started', 'started_at': session.started_at})

    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        session = self.get_object()
        if session.status == 'completed':
            return Response({'detail': 'Session is already completed.'}, status=status.HTTP_400_BAD_REQUEST)
        session.complete()
        return Response({'status': 'Session completed', 'ended_at': session.ended_at})

class CodingChallengeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List and retrieve active coding challenges.
    """
    queryset = CodingChallenge.objects.filter(is_active=True)
    serializer_class = CodingChallengeSerializer
    permission_classes = [permissions.IsAuthenticated]

class ChallengeSubmissionViewSet(viewsets.ModelViewSet):
    """
    Manage coding challenge submissions for the authenticated user.
    """
    serializer_class = ChallengeSubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ChallengeSubmission.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        submission = serializer.save(user=self.request.user)
        # Simply calculate basic score based on the model's logic
        submission.calculate_score()
