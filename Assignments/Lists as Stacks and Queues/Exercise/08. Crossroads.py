from collections import deque

green_light_time = int(input())
free_window_time = int(input())

cars = deque()
crashed = False
total_cars_passed = 0

line = input()

while line != "END":
    if line == "green":
        green_light_timer = green_light_time
        if cars:
            current_car_name = cars.popleft()
            current_car = deque(current_car_name)
            while green_light_timer:
                if not current_car:
                    if cars:
                        current_car_name = cars.popleft()
                        current_car = deque(current_car_name)
                    else:
                        break

                current_car.popleft()
                green_light_timer -= 1

            if current_car:
                free_window_timer = free_window_time
                while free_window_timer and current_car:
                    current_car.popleft()
                    free_window_timer -= 1

                if current_car:
                    crashed = True
                    print("A crash happened!")
                    print(f"{current_car_name} was hit at {current_car.popleft()}.")
                    break

    else:
        cars.append(line)
        total_cars_passed += 1

    line = input()

if not crashed:
    print(f"Everyone is safe.")
    print(f"{total_cars_passed - len(cars)} total cars passed the crossroads.")
