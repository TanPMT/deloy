from django.db import connection
from django.core.management import call_command

def initialize_db():
    with connection.cursor() as cursor:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        if not cursor.fetchall():
            call_command('migrate')
            # Thêm dữ liệu ban đầu nếu cần
            # Ví dụ: call_command('loaddata', 'initial_data.json')

initialize_db()
