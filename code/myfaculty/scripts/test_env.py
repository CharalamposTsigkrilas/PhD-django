from django.conf import settings
from myprofile.models import StaffMember, Associate
from django.contrib.auth import get_user_model
from datetime import datetime

person = {

    'email' : 'thkam@hua.gr',
    'given_name' : 'Θωμάς', 
    'surname' : 'Καμαλάκης',
    'fathers_name' : 'Σπυρίδωνα',
    'date_of_birth' : '01/09/1975',
    
    'tin' : '3959764',
    'ssn' : '295894765',

    'is_internal' : 'True',
    
    'institution' : 'Χαροκόπειο Πανεπιστήμιο',
    'school' : 'Ψηφιακής Τεχνολογία',
    'department' : 'Πληροφορικής και Τηλεματικές',
    
    'title' : 'Καθηγητής',
    
    'home_address_street' : 'Παραδείσου',
    'home_address_no' : '17',


    'home_address_po_box' : '15125',
    'home_address_city' : 'Μαρούσι, Αθήνα',
    'home_address_country' : 'Ελλάδα',
    'mobile_phone' : '94867654',
    'home_phone' : '93586573',

    'work_address_street' : '',
    'work_address_no' : '',
    'work_address_po_box' : '',
    'work_address_city' : '',
    'work_address_country' : '',
    'work_phone' : '',
}

associate = {

    'email' : 'thomaskamalakis@gmail.com',
    'given_name' : 'Θωμάς', 
    'surname' : 'Καμαλάκης',
    'fathers_name' : 'Σπυρίδωνα',
    'date_of_birth' : '01/09/1900',
    
    'tin' : '3959764',
    'ssn' : '295894765',

    'is_phd_student' : 'True',
    'is_postdoc' : 'False',
    
    
    'home_address_street' : 'Παραδείσου',
    'home_address_no' : '17',
    'home_address_po_box' : '15125',
    'home_address_city' : 'Μαρούσι, Αθήνα',
    'home_address_country' : 'Ελλάδα',
    'mobile_phone' : '94867654',
    'home_phone' : '93586573',

    'work_phone' : '2109549406',
}

def translate_to_staff(s):
    d = {}
    for k, v in s.items():
        if v != '':            
            if k in ['home_address_no', 'home_address_po_box', 'work_address_no', 'work_address_po_box']:
                val = int(v)
            elif k in ['date_of_birth']:
                val = datetime.strptime(v, '%d/%m/%Y')
            else:
                val = v
            d[k] = val

    return StaffMember(**d)

def translate_to_associate(s):
    d = {}
    for k, v in s.items():
        if v != '' :            
            if k in ['home_address_no', 'home_address_po_box', 'work_address_no', 'work_address_po_box']:
                val = int(v)
            elif k in ['date_of_birth']:
                val = datetime.strptime(v, '%d/%m/%Y')
            else:
                val = v
            d[k] = val

    return Associate(**d)

def run():
    # Create superuser

    User = get_user_model()
    if not User.objects.filter(username = 'admin').exists():
        User.objects.create_superuser('admin', 'thomaskamalakis@gmail.com', 'hua123##')

    if not StaffMember.objects.filter(email = person['email']).exists():
        E = translate_to_staff(person)
        # Check to see whether a user already exists

        username = E.email.split('@')[0]
        email = E.email
        u_query = User.objects.filter(username = username)
        if u_query.count() == 0:
            u = User(username = username, 
                    email = email)
            u.save()
        else:
            u = u_query[0]

        E.user = u
        E.save()

    if not Associate.objects.filter(email = person['email']).exists():
        A = translate_to_associate(associate)

        username = A.email.split('@')[0]
        email = A.email
        u_query = User.objects.filter(username = username)
        if u_query.count() == 0:
            u = User(username = username, 
                    email = email)
            u.save()
        else:
            u = u_query[0]

        A.user = u
        A.save()

        
      

    
