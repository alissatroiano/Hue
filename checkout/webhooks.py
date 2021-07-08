from django.http import HttpResponse


class StripeWH_Handler:
    """ stripe webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handles unexpected/generic/unknown events
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
