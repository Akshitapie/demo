from datetime import datetime

from django.http import HttpResponse

def index(request):
    try:
        now = datetime.now()
        html = f"""
        <html>
            <body>
                <h1>Hello from Vercel!</h1>
                <p>The current time is { now }.</p>
            </body>
        </html>
        """
        return HttpResponse(html)
    except Exception as e:
        error_message = "An error occurred while processing the request."
        return HttpResponse(error_message, status=500)
