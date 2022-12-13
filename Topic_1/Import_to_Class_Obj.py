from Topic_1.County import County
import csv

county = {}

with open('Iowa 2010 Census Data Population Income.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            continue
        elif row[1] == 'Iowa State' or row[1] == 'United States':
            line_count += 1
            continue
        county[str(row[1])] = County(row[0], row[1], row[2], row[3], row[4], row[5], row[6])


def find_county_pop_per_household(county_name):
    county_obj = county.get(county_name)
    county_pop = int(county_obj.population.replace(',', ''))
    county_households = int(county_obj.number_of_households.replace(',', ''))
    return county_obj.county + ' County: ' + "{:.2f}".format(county_pop / county_households) + ' people per household.'


# Driver
print(find_county_pop_per_household('Dallas'))
total_pop = 0
for key in county:
    total_pop += int(county[key].population.replace(',',''))
print(str(total_pop))

