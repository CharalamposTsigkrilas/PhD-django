# Management System for the Department of Informatics and Telematics, Harokopio University of Athens (DIT HUA) with Django

## Overview

This project is a **Django-based monolithic web application** for managing all members, study programs, theses and projects of the Department of Informatics.

It provides authentication and role-based access for administrators, secretaries, staff members, associates, students and now **PhD students**.

The system can be deployed locally for development using **Docker Compose**, with containers for the Django web app and a PostgreSQL database.

## Features

- Authentication system with Login
- Role-based access control
- Integrated CRUD management for:

  - Curriculum
  - Assosiates
  - Leaves
  - Theses
  - Projects
  - Timesheets

- Email sending system
- Media & file uploads
- Persistent data storages
- Role-based user profiles:

  - Secretary
  - Staff Member
  - Student
  - Associate

- `New` Integrated CRUD management for **PhD Students** (via the `phds` app):

  - **PhD Student Profile** with image uploads
  - **Journal Publications**
  - **Conference Publications**
  - **Teaching & Supporting Activities** (e.g. tutorials in undergraduate courses)
  - **Annual Reports** with .pdf file uploads

## Technologies

- **Backend:** Python 3 (Django)
- **Database:** PostgreSQL
- **Frontend:** Django Templates (HTML, CSS, JS) & Crispy Forms
- **Containers:** Docker, Docker Compose
- **Email:** Google Cloud API

## Setup Guide (Linux recommended)

### 1. Clone or Download as a zip this repository to your machine

### 2. Create an `.env` environment file

In the project root directory, create an `.env` file and add the following environment variables (replace `<>` with your values):

```
POSTGRES_DB=<db_name>
POSTGRES_USER=<db_user_name>
POSTGRES_PASSWORD=<db_user_password>

AUTH_LDAP_SERVER_URI=<server_uri>
AUTH_LDAP_BIND_DN=<bind_dn>
AUTH_LDAP_BIND_PASSWORD=<bind_password>

STUD_IP=<ip>
STUD_USER=<user>
STUD_PASSWORD=<password>
STUD_DATABASE=<db_name>
```

### 3. Configure Gmail API credentials

Inside `code/myfaculty/mailer/` create a folder named `auth` and place the following files inside:

- `ditdean_gmail.json`
- `ditdean_token.json`

Follow Google’s guide for setting them up:
[Quickstart with Gmail API(Python)](https://developers.google.com/gmail/api/quickstart/python).

Then create a `gmail.py` file in `code/myfaculty/mailer/auth/` with this implementation:

```
import mimetypes
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from django.conf import settings
import base64
from email.message import EmailMessage

SCOPES = ['https://mail.google.com/']

class gmailapi:

    # Replace <> with your gmail sender
    def __init__(self, token_file = 'mailer/auth/ditdean_token.json', credentials_file = 'mailer/auth/ditdean_gmail.json', from_ad = '<mail@gmail.com>'):
        self.from_ad = from_ad
        try:
            creds = None
            if os.path.exists(token_file):
                creds = Credentials.from_authorized_user_file(token_file, SCOPES)

            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        credentials_file, SCOPES)
                    creds = flow.run_local_server(port = 0)
                with open(token_file, 'w') as token:
                    token.write(creds.to_json())

            self.service = build('gmail', 'v1', credentials = creds)

        except HttpError as error:
            print(f'An error occurred: {error}')

    def build_message(self, to, subject, body, cc=None):
        message = EmailMessage()

        message['To'] = to
        message['From'] = self.from_ad
        message['Subject'] = subject
        if cc:
            message['Cc'] = cc
        body += '\n'
        body += settings.EMAIL_PLATFORM_URL

        message.set_content( body )
        return message

    def build_draft(self, message):
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        create_message = {
            'message': {
                'raw': encoded_message
            }
        }
        draft = self.service.users().drafts().create(userId = "me",
                                                body = create_message).execute()
        return draft

    def create_draft(self, to, subject, body, cc=None):
        message = self.build_message(to, subject, body, cc=cc)
        return self.build_draft(message)

    def create_draft_with_attachments(self, to, subject, body, attachments = [], cc=None):
        message = self.build_message(to, subject, body, cc=cc)

        for attachment in attachments:
            type_subtype, _ = mimetypes.guess_type(attachment)
            maintype, subtype = type_subtype.split('/')

            with open(attachment, 'rb') as f:
                data = f.read()
                filename = os.path.basename( attachment )
            message.add_attachment(data, maintype, subtype, filename = filename)
        return self.build_draft( message )

    def send(self, to, subject, body, attachments = [], cc=None):
        draft_dict = self.create_draft_with_attachments(to, subject, body, attachments = attachments, cc=cc)
        id = draft_dict['id']
        draft = self.service.users().drafts().send(body = {'id': id}, userId = 'me').execute()

def notify(to, subject, body, cc=None, attachments=[]):
    g = gmailapi()
    g.send(to, subject, body, attachments=attachments, cc=cc)
```

### Important!

The `.env` file and the `auth` folder must remain local. They are excluded from version control (GitHub/GitLab).

---

## Installation & Usage

### Start the project

#### First-time build and start the containers:

```bash
docker-compose up --build
```

#### On subsequent runs just start the containers:

```bash
docker-compose up
```

---

### Post-startup (use an idle terminal)

#### Create a superuser:

```bash
docker-compose exec web python manage.py createsuperuser
```

#### (Optional) Load initial data from a .json file

Create a file named `default.json` in `code/myfaculty/`.

#### Run it with:

```bash
docker-compose exec web python manage.py loaddata default.json
```

#### (Optional) Set users’ passwords via a script

Unrestricted users' passwords can only be set with a python script. Create `initialization.py` in `code/myfaculty/`:

```
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myfaculty.settings')
django.setup()

from django.contrib.auth.models import User

# Give all users a password with acceptable form

# Example: set password for user with primary key <pk>
user_1 = User.objects.get(pk=<pk>)
user_1.set_password("user_password")
user_1.save()
```

#### Run it with:

```bash
docker-compose exec web python initialization.py
```

#### Note!

The `default.json` and `initialization.py` files are excluded from version control (GitHub/GitLab).

---

### Open the App

After the project has been built and started successfully, the application’s UI is available.

> To use the system’s functionalities, make sure at least one user or superuser (admin) has been created.

The app runs at [http://localhost:30082](http://localhost:30082).

---

### Stop the project (use an idle terminal)

#### Stop containers:

```bash
docker-compose down
```

#### Stop and remove containers & volumes:

```bash
docker-compose down --volumes
```

---

### Rebuilding the project

#### Fix database permissions if needed:

```bash
sudo chmod -R 755 ./data/db
```

#### Or delete the database completely:

```bash
sudo rm -r ./data/db
```

---

## Credits

**Contributors**:

- Tsigkrilas Charalampos, Student of DIT HUA
- Thomas Kamalakis, Dean of DIT HUA

---

## References

- Official App: [mydep.ditapps.hua](https://mydep.ditapps.hua.gr)
- Official GitLab Repository: [My Faculty](https://gitlab.com/thkam/myfaculty_pub)
