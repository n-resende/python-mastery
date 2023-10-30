# cta.py

import readrides
from collections import Counter
import tracemalloc

def find_total_number_of_bus_routes(bus_data):
    
    bus_routes = Counter()
    for x in bus_data:
        bus_routes[x['route']] = 0
        
    print(f'Number of bus routes in Chicago: {len(bus_routes)}')

def find_total_rides_of_route_on_date(bus_data, route, date):
    route_data = [x for x in bus_data if x['route'] == route and x['date'] == date]
    
    if route_data:
        print(f"The number of rides for route {route} on the date {date} was {route_data[0]['rides']}")
    else:
        print(f'There were no rides for the given route and date')

def find_total_number_of_rides_per_route(bus_data):
    
    bus_routes = Counter()
    for x in bus_data:
        bus_routes[x['route']] += x['rides']
    
    for route,rides in bus_routes.most_common():
        print(f"Route: {route} | Rides: {rides}")
    
def greatest_five_ten_year_increase(bus_data):
    first = Counter()
    second = Counter()
    
    for x in bus_data:
        if x['date'][-4:] == '2001':
            first[x['route']] += x['rides']
        elif x['date'][-4:] == '2011':
            second[x['route']] += x['rides']
            
    diff = second - first
    for route, dif in diff.most_common(5):
        print(f'Route: {route} | Difference: {dif}')

if __name__ == '__main__':
    tracemalloc.start()
    bus_data = readrides.read_rides_as_dictionaries('Data/ctabus.csv')
    
    # 1. How many bus routes exist in Chicago?
    find_total_number_of_bus_routes(bus_data)
    
    # 2. How many people rode the number 22 bus on February 2, 2011?  What about any route on any date of your choosing?
    target_route = '22'
    target_date = '02/02/2011'
    find_total_rides_of_route_on_date(bus_data, target_route, target_date)

    # 3. What is the total number of rides taken on each bus route?
    find_total_number_of_rides_per_route(bus_data)
    
    # 4. What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?
    greatest_five_ten_year_increase(bus_data)
    
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
