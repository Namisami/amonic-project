import os
import csv
from datetime import datetime

from core.settings import BASE_DIR
from airports.models import Schedule, Route, Airport, Aircraft

CSV_ROOT = BASE_DIR / 'media'

def schedule_import(file):
    successful = 0
    duplicate = 0
    errors = 0
    with open(os.path.join(CSV_ROOT, file)) as f:
        reader = csv.reader(f)
        for row in reader:
            try:
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
                    schedule, created = Schedule.objects.get_or_create(
                        date=date,
                        time=time,
                        aircraft=aircraft,
                        route=route,
                        flight_number=row[4][0] + row[5][0] + row[3],
                        economy_price=int(row[6][:-3]),
                    )
                    schedule.confirmed = True if row[7] == 'OK' else False
                    schedule.save()
                    if created:
                        successful += 1
                    else:
                        duplicate += 1
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
                        successful += 1
            except:
                errors += 1
                continue
    print({
        'successful': successful,
        'duplicate': duplicate,
        'errors': errors
    })
    return {
        'successful': successful,
        'duplicate': duplicate,
        'errors': errors
    }