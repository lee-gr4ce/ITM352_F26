# Calculate fare totals and maximum trip distance for fares over $10.

import csv

filename = 'taxi_1000.csv'

with open(filename, 'r') as file:
    csv_reader = csv.reader(file)

    total_fare = 0.0
    max_distance = 0.0
    average_fare = 0.0
    num_fares = 0

    for row_number, row in enumerate(csv_reader):
        if row_number == 0:
            fare_index = row.index('Fare')  # Find the index of the fare column
            distance_index = row.index('Trip Miles')  # Find the index of the distance column
            continue

        fare = float(row[fare_index])
        if fare > 10:
            distance = float(row[distance_index])
            total_fare += fare
            num_fares += 1

            if distance > max_distance:
                max_distance = distance

    if num_fares > 0:
        average_fare = total_fare / num_fares

print(f'Total Fare: ${total_fare:.2f}')
print(f'Average Fare: ${average_fare:.2f}')
print(f'Max Trip Distance: {max_distance:.2f} miles')