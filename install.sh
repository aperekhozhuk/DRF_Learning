#!/bin/bash


# Creating virtual envirnoment
python3 -m venv env
source env/bin/activate
# Installing dependencies
pip install -r requirements.txt


# Path to project folder which contains 'manage.py' file
project_path="project"
# Credentials of superuser
name="admin"
email="admin@example.com"
password="password"

# Creating DB
project_manage_file_path="python3 ${project_path}/manage.py "
migrate_command="${project_manage_file_path} migrate"
eval "${migrate_command}"

# Make supersuser's credentials string
super_user_creds="'${name}', '${email}', '${password}'"

# Python commands for creating superuser
import_command="from django.contrib.auth.models import User;"
create_superuser_command="User.objects.create_superuser(${super_user_creds});"

# Django shell command
django_shell_command="${project_manage_file_path} shell"

# Creating total bash command
command="${import_command} ${create_superuser_command}"
total_command="echo \"${command}\" | ${django_shell_command}"

# Finally running
eval "${total_command}" > /dev/null 2>&1
exit 0
