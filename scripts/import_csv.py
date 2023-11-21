import os
import csv
from datetime import datetime

from core.settings import BASE_DIR
from users.forms import UserCreationForm
from users.models import Role, Office
from airports.models import Schedule, Route, Airport, Aircraft, Survey, CabinType

CSV_ROOT = BASE_DIR / 'csv_data'

def run():
    with open(os.path.join(CSV_ROOT, 'UserData.csv')) as f:
        reader = csv.reader(f)
        for row in reader:
            role, _ = Role.objects.get_or_create(
                title=row[0]
            )
            office, _ = Office.objects.get_or_create(
                title=row[5]
            )
            dt = datetime.strptime(row[6], '%m/%d/%Y').strftime('%Y-%m-%d')
            user_dict = {
                'role': role,
                'email': row[1],
                'password1': row[2],
                'password2': row[2],
                'first_name': row[3],
                'last_name': row[4],
                'office': office,
                'date_of_birth': dt,
                'is_active': bool(int(row[7]))
            }
            form = UserCreationForm(user_dict)
            try:
                if form.is_valid():
                    form.save()
            except Exception as e:
                print('ERROR', e)

    schedule_files = ['Schedules_V12.csv', 'Schedules_V12_2.csv']
    for file in schedule_files:
        with open(os.path.join(CSV_ROOT, file)) as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 9:
                    del row[6]
                action = row[0]
                try:
                    date = datetime.strptime(row[1], '%Y-%m-%d').strftime('%Y-%m-%d')
                    time = datetime.strptime(row[2], '%H:%M').strftime('%H:%M:00')
                except ValueError:
                    continue

                aircraft, _ = Aircraft.objects.get_or_create(
                    name=row[3]
                )

                departure_airport, _ = Airport.objects.get_or_create(
                    iata_code=row[4]
                )
                arrival_airport, _ = Airport.objects.get_or_create(
                    iata_code=row[5]
                )


                route, _ = Route.objects.get_or_create(
                    departure_airport=departure_airport,
                    arrival_airport=arrival_airport,
                    distance=int(row[3]),
                    flight_time=100
                )
                if action == 'ADD':
                    schedule, _ = Schedule.objects.get_or_create(
                        date=date,
                        time=time,
                        aircraft=aircraft,
                        route=route,
                        flight_number=row[4][0] + row[5][0] + row[3],
                        economy_price=int(row[6][:-3]),
                    )
                    schedule.confirmed = True if row[7] == 'OK' else False
                    schedule.save()
                elif action == 'EDIT':
                    try:
                        schedule = Schedule.objects.get(
                            date=date,
                            time=time,
                            aircraft=aircraft,
                            route=route,
                            flight_number=row[4][0] + row[5][0] + row[3],
                            economy_price=int(row[6][:-3]),
                        )
                    except Schedule.DoesNotExist:
                        schedule = None
                    if schedule:
                        schedule.confirmed = True if row[7] == 'OK' else False
                        schedule.save()
                        
    survey_files = ['survey_05.csv']
    # survey_files = ['survey_05.csv', 'survey_06.csv', 'survey_07.csv']
    for file in survey_files:
        with open(os.path.join(CSV_ROOT, file)) as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                if row[0] != '':
                    departure_airport, _ = Airport.objects.get_or_create(
                        iata_code=row[0]
                    )
                else:
                    departure_airport=None
                if row[1] != '':
                    arrival_airport, _ = Airport.objects.get_or_create(
                        iata_code=row[1]
                    )
                else:
                    arrival_airport = None

                if row[4] != '':
                    travel_class, _ = CabinType.objects.get_or_create(
                        name=row[4]
                    )
                else:
                    travel_class = None

                survey, _ = Survey.objects.get_or_create(
                    departure=departure_airport,
                    arrival=arrival_airport,
                    age=int(row[2]) if row[2] != '' else None,
                    gender=row[3] if row[3] != '' else 'NS',
                    travel_class=travel_class,
                    q1=row[5] if row[5] != '' else None,
                    q2=row[6] if row[6] != '' else None,
                    q3=row[7] if row[7] != '' else None,
                    q4=row[8] if row[8] != '' else None,
                )