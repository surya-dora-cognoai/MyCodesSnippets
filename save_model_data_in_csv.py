mport csv
from datetime import datetime
from EasyChatApp.models import APIElapsedTime
from django.conf import settings

def cronjob():
    try:
        print('start')
        start_date = "2024-04-23"
        print("start_date", start_date)
        end_date = "2024-04-30"
        print("end_date", end_date)
        file_name= settings.MEDIA_ROOT + f"Prod_analytics_logs.csv"
        print("file_name", file_name)
        start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
        end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')

        logs = APIElapsedTime.objects.filter(api_name='CRM API',created_at__range=(start_date_obj, end_date_obj)).iterator()

        field_mapping = {
            "request_packet": "Request Packet",
            "response_packet": "Response Packet",
            "created_at": "Created Time",
            "api_status_code": "Api StatusCode",
            "api_status": "Api Status"
        }

        with open(file_name, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_mapping.values())
            writer.writeheader()
            for log in logs:
                writer.writerow({field_mapping[field]: getattr(log, field) for field in field_mapping.keys()})
        print("end")
    except Exception as e:
        print("e", e)



cronjob()
