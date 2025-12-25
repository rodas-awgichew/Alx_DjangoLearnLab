from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Notification

class NotificationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.filter(
            recipient=request.user
        ).order_by('-timestamp')

        data = [
            {
                'actor': n.actor.username,
                'verb': n.verb,
                'is_read': n.is_read,
                'timestamp': n.timestamp
            }
            for n in notifications
        ]

        return Response(data)
