vehicle = {'car3': [1, 3, False], 'car3_ac': [1, 3, True], 'car4': [1, 4, False], 'car4_ac': [1, 4, True],
           'van6': [1, 6, False], 'van6_ac': [1, 6, True], 'van8': [1, 8, False], 'van8_ac': [1, 8, True],
           'three_wheeler': [1, 3, False], 'truck7': [1, 0, False], 'truck12': [1, 0, False],
           'lorry 25': [1, 0, False], 'lorry 35': [1, 0, False]}
options = 0

seat_opt = int(input('Enter the number of seats needed: '))
ac_opt = input('Enter if needed (Y/n): ')

if ac_opt.lower() == 'y':
    if seat_opt <= 3 and seat_opt > 0:
        # for veh, amt, seat, ac in vehicle:
        #     if
        if vehicle.get('car3_ac') > 0:
            options = options + 1
            print(f"{options}. car\tCapacity: {vehicle.get('car3_ac')}passengers\tAC")


        else:
            print('Sorry no vehicles available')


    if seats == 4


