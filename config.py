import os
from urllib.parse import urlencode

from dotenv import load_dotenv

load_dotenv()

SERVICEM8_CLIENT_ID = os.getenv("SERVICEM8_CLIENT_ID")
SERVICEM8_CLIENT_SECRET = os.getenv("SERVICEM8_CLIENT_SECRET")
# SERVICEM8_REDIRECT_URI = os.getenv("SERVICEM8_REDIRECT_URI")
# SERVICEM8_AUTH_URL = os.getenv("SERVICEM8_AUTH_URL")
# SERVICEM8_TOKEN_URL = os.getenv("SERVICEM8_TOKEN_URL")
# TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
# GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")

BASE_URL = "https://api.servicem8.com/api_1.0"

SCOPE = [
    "staff_locations",
    "staff_activity",
    "publish_sms",
    "publish_email",
    "vendor",
    "vendor_logo",
    "vendor_email",
    "read_locations",
    "manage_locations",
    "read_staff",
    "manage_staff",
    "read_customers",
    "manage_customers",
    "read_customer_contacts",
    "manage_customer_contacts",
    "read_jobs",
    "manage_jobs",
    "create_jobs",
    "read_job_contacts",
    "manage_job_contacts",
    "read_job_materials",
    "manage_job_materials",
    "read_job_categories",
    "manage_job_categories",
    "read_job_queues",
    "manage_job_queues",
    "read_tasks",
    "manage_tasks",
    "read_schedule",
    "manage_schedule",
    "read_inventory",
    "manage_inventory",
    "read_job_notes",
    "publish_job_notes",
    "read_job_photos",
    "publish_job_photos",
    "read_job_attachments",
    "publish_job_attachments",
    "read_inbox",
    "read_messages",
    "manage_notifications",
    "manage_templates",
    "manage_badges",
    "read_assets",
    "manage_assets"
]


# def get_oauth_login_url():
#     params = {
#         "client_id": SERVICEM8_CLIENT_ID,
#         "redirect_uri": SERVICEM8_REDIRECT_URI,
#         "response_type": "code",
#         "scope": " ".join(SCOPE)  # Adjust based on required scopes
#     }
#     return f"{SERVICEM8_AUTH_URL}?{urlencode(params)}"


DEFAULT_JOB_QUEUE = "303c135a-2150-4a12-9a6b-228db8019d8b"
