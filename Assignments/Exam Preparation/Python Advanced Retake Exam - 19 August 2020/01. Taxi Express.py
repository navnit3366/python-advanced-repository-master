from collections import deque

customers = deque(int(x) for x in input().split(', '))
taxi_drivers = deque(int(x) for x in input().split(', '))
total_time = 0

while True:
    current_customer = customers.popleft()
    current_taxi_driver = taxi_drivers.pop()

    if current_customer <= current_taxi_driver:
        total_time += current_customer

    else:
        customers.appendleft(current_customer)

    if len(customers) == 0:
        print('All customers were driven to their destinations')
        print(f'Total time: {total_time} minutes')
        break

    elif len(taxi_drivers) == 0 and len(customers) > 0:
        print('Not all customers were driven to their destinations')
        print(f'Customers left: {", ".join([str(x) for x in customers])}')
        break