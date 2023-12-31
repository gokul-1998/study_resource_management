from celery import shared_task
from .models import StudyResource
import flask_excel as excel
from .mail_service import send_message
from .models import User, Role
from jinja2 import Template
from celery import shared_task

@shared_task(ignore_result=False)
def create_resource_csv():
    import time
    time.sleep(20)
    stud_res = User.query.with_entities(
        User.email, User.username).all()

    csv_output = excel.make_response_from_query_sets(
        stud_res, ["email", "username"], "csv")
    filename = "test.csv"

    with open(filename, 'wb') as f:
        f.write(csv_output.data)

    return filename


@shared_task(ignore_result=True)
def daily_reminder(to, subject):
    users = User.query.filter(User.roles.any(Role.name == 'admin')).all()
    for user in users:
        with open('test.html', 'r') as f:
            template = Template(f.read())
            send_message(user.email, subject,
                         template.render(email=user.email))
    return "OK"
