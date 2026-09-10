import os
import requests

from django.core.mail.backends.base import BaseEmailBackend
from django.core.mail import EmailMessage


class ResendEmailBackend(BaseEmailBackend):

    def send_messages(self, email_messages):
        if not email_messages:
            return 0

        sent_count = 0

        api_key = os.getenv("RESEND_API_KEY")

        if not api_key:
            if not self.fail_silently:
                raise ValueError("RESEND_API_KEY is not configured.")
            return 0

        for message in email_messages:
            try:
                response = requests.post(
                    "https://api.resend.com/emails",
                    headers={
                        "Authorization": f"Bearer {api_key}",
                        "Content-Type": "application/json",
                    },
                    json={
    "from": "onboarding@resend.dev",
    "to": ["delivered@resend.dev"],
    "subject": message.subject,
    "html": message.body,
},
                    timeout=10,
                )

                response.raise_for_status()
                sent_count += 1

            except requests.RequestException:
                if not self.fail_silently:
                    raise

        return sent_count