from _collections import  deque

def next_sec(hours,minutes,seconds):
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0

    if minutes == 60:
        hours += 1
        minutes = 0

    if hours == 24:
        hours = 0

    return hours,minutes,seconds

robot_info = input().split(';')
robots_times = {}
available = deque()
waiting = deque()
time = [int(x) for x in input().split(':')]
products = deque()

product = input()

while product != 'End':
    products.append(product)
    product = input()

    for r in robot_info:
        robot_name = r.split('-')[0]
        robot_time = int(r.split('-')[1])
        available.append([robot_name,robot_time])
        robots_times[robot_name] = robot_time

while products:
    for robot in waiting:
        robot_name = robot[0]
        robot[1] -= 1
        if robot[1] <= 0:
            available.append([robto_name , robots_times[robto_name]])

    #filters robots with less than 0 wait time
    waiting = [i for i in waiting if i[1] > 0]

    time  = next_sec(time[0] , time[1] , time[2])
    current_product = products.popleft()

    if not available:
        products.append(current_product)
        continue

    current_robot = available.popleft()
    print(f"{current_robot[0]} - {current_product} [{time[0]:02d}:{time[1]:02d}:{time[2]:02d}]")
    waiting.append(current_robot)