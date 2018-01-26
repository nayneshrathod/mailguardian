from .models import Message, Headers, SpamReport, RblReport, McpReport, MailscannerReport
from .serializers import MessageSerializer, HeaderSerializer, SpamReportSerializer, RblReportSerializer, McpReportSerializer, MailscannerReportSerializer
from mailware.pagination import PageNumberPaginationWithPageCount
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    model = Message
    pagination_class = PageNumberPaginationWithPageCount
    permission_classes = (IsAuthenticated,)

class HeaderViewSet(viewsets.ModelViewSet):
    queryset = Headers.objects.all()
    serializer_class = HeaderSerializer
    model = Headers
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.query_params.__contains__('message'):
            return self.queryset.filter(message_id=self.request.query_params.get('message'))
        else:
            return self.queryset

class SpamReportViewSet(viewsets.ModelViewSet):
    queryset = SpamReport.objects.all()
    serializer_class = SpamReportSerializer
    model = SpamReport
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.query_params.__contains__('message'):
            return self.queryset.filter(message_id=self.request.query_params.get('message'))
        else:
            return self.queryset

class RblReportViewSet(viewsets.ModelViewSet):
    queryset = RblReport.objects.all()
    serializer_class = RblReportSerializer
    model = RblReport
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.query_params.__contains__('message'):
            return self.queryset.filter(message_id=self.request.query_params.get('message'))
        else:
            return self.queryset

class MailscannerReportViewSet(viewsets.ModelViewSet):
    queryset = MailscannerReport.objects.all()
    serializer_class = MailscannerReportSerializer
    model = MailscannerReport
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.query_params.__contains__('message'):
            return self.queryset.filter(message_id=self.request.query_params.get('message'))
        else:
            return self.queryset

class McpReportViewSet(viewsets.ModelViewSet):
    queryset = McpReport.objects.all()
    serializer_class = McpReportSerializer
    model = McpReport
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.query_params.__contains__('message'):
            return self.queryset.filter(message_id=self.request.query_params.get('message'))
        else:
            return self.queryset