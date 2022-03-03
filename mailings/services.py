from untitled_shop import settings
from mailchimp3 import MailChimp


def get_mailchimp_client():
    return MailChimp(
        mc_api=settings.MAILCHIMP_API_KEY,
        mc_user=settings.MAILCHIMP_USERNAME
    )

