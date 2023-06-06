vehicle = {'Three-Wheeler3_no': [1, 3, 'Non-AC'], 'Car3_no': [1, 3, 'Non-AC'], 'Car3_ac': [1, 3, 'AC'], 'Car4_no': [1, 4, 'Non-AC'], 'Car4_ac': [1, 4, 'AC'],
           'Van6_no': [1, 6, 'Non-AC'], 'Van6_ac': [1, 6, 'AC'], 'Van8_no': [1, 8, 'Non-AC'], 'Van8_ac': [1, 8, 'AC'],
           'Truck7_no': [1, -7, 'Non-AC'], 'Truck12_no': [1, -12, 'Non-AC'],
           'Lorry25_no': [1, -25, 'Non-AC'], 'Lorry35_no': [1, -35, 'Non-AC']}
condition = {'y': 'AC', 'n': 'Non-AC'}
options = []
run = 0


class Employee:
    def __init__(self, empID, name, contact_no):
        self.id = empID
        self.name = name
        self.contact_no = contact_no


def consumer():
    index = 0
    seat_opt = int(input('Enter the number of seats needed: '))
    ac_opt: str = input('Enter if AC needed (Y/n): ')

    for veh in vehicle:
        amt, seat, ac = vehicle.get(veh)
        if (seat_opt <= seat > 0 and condition.get(ac_opt.lower()) == ac and amt > 0 and index < 2):
            index = index + 1
            options.append(f"{index}. {veh[:-4]:16}\tCapacity: {seat} passengers\t\t {ac}")

    for i in options:
        print(i)
    choice = int(input('Enter your choice: '))
    print(f'Your choice is \n{options[choice - 1]}\n')

    if len(options) > 0 and choice > 0:
        confirm = input('Would you like confirm your choice (Yes/ no): ')

        if confirm.lower() == 'yes':
            confirm_data = str(options[choice - 1]).split(' ')
            co_veh = str(confirm_data[1]) + str(confirm_data[-3]) + '_' + str(confirm_data[-1][0:2]).lower()
            vehicle[co_veh][0] = vehicle[co_veh][0] -1
            print('Vehicle has been confirmed :)\n')

        elif confirm.lower() == 'no':
            print('Order cancelled..\n')




def utility():
    index = 0
    print('Enter vehicle type: ')
    print('\t1. Truck (7ft and 12ft)')
    print('\t2. Lorry(25000kg and 35000kg)')
    uti_in = int(input('>>> '))

    if uti_in == 1:
        size_opt = input('Enter the required length (7ft/ 12ft): ')
        size_opt = (-1 * int(size_opt[:-2]))

        for veh in vehicle:
            amt, size, ac = vehicle.get(veh)
            if (size_opt >= size > -13 and amt > 0 and index < 1):
                index = index + 1
                options.append(f"{index}. {veh[:-4]:16}\tlength: {abs(size)} \t\t {ac}")

    elif uti_in == 2:
        size_opt = input('Enter the required load (23T/ 35T): ')
        size_opt = (-1 *int(size_opt[:-1]))
        for veh in vehicle:
            amt, size, ac = vehicle.get(veh)
            if (size_opt >= size > -36 and amt > 0 and index < 1):
                index = index + 1
                options.append(f"{index}. {veh[:-4]:16}\tlength: {size}")

    for i in options:
        print(i)
    choice = int(input('Enter your choice: '))
    print(f'Your choice is \n{options[choice - 1]}\n')

    if len(options) > 0 and choice > 0:
        confirm = input('Would you like confirm your choice (Yes/ no): ')

        if confirm.lower() == 'yes':
            confirm_data = str(options[choice - 1]).split(' ')
            co_veh = str(confirm_data[1]) + str(confirm_data[-3]) + '_' + str(confirm_data[-1][0:2]).lower()
            vehicle[co_veh][0] = vehicle[co_veh][0] - 1
            print('Vehicle has been confirmed :)\n')

        elif confirm.lower() == 'no':
            print('Order cancelled..\n')

def admin():
    admin = 'Dinushi'
    password = 'dinu321'
    verify_count = 0

    def admin_option():
        emp = []
        emp_id = 1

        emp.append(Employee(emp_id, admin, '0123456789'))

        print('-----------')
        print('Admin Panel')
        print('-----------\n')
        print('Enter option:')
        print('\t 1. Add a vehicle:')
        print('\t 2. remove a vehicle:')
        print('\t 3. Assign a job')
        print('\t 4. remove a job')
        print('\t 5. Exit admin panel')
        opt = int(input('>>> '))

        if opt == 1 or opt == 2:
            type = input('Vehicle type: ')
            num = input('Number of seats or vehicle size: ')
            ac_opt = input('AC or Non-AC, enter -> (ac/ no): ')
            amt = int(input('amount of vehicles: '))
            veh = type.title() + num + '_' + ac_opt
            # print(veh)

            if opt == 1:
                vehicle[veh][0] = vehicle[veh][0] + amt

            elif opt == 2:
                vehicle[veh][0] = vehicle[veh][0] - amt
            print(
                f"{type :16}\tCapacity/ Size: {abs(vehicle[veh][1])}\t\t{vehicle[veh][2]}\t\t{vehicle[veh][0]} available")

        elif opt == 3:
            emp_id = emp_id + 1
            emp_name = input('Enter employee name: ')
            emp_contact = input('Enter employee contact: ')
            emp.append(Employee(emp_id, emp_name, emp_contact))
            print(f"{str(emp_id).zfill(2)}\t\t{emp_name:12}\t{emp_contact}")
            print('Entry added')

        elif opt == 4:
            emp_name = input('Enter employee name: ')
            for obj in emp:
                if obj.name == emp_name:
                    print(f"{str(obj.id).zfill(2)}\t\t{obj.name:12}\t{obj.contact_no}")
                    del obj
                    print('Entry removed')

        elif opt == 5:
            pass

        return 3

    while verify_count < 3:
        user = input('Enter username: ')
        pwd = input('Enter password: ')

        if user == admin and pwd == password:
            verify_count = admin_option()

        else:
            print('Incorrect username or Password!\n')
            verify_count = verify_count + 1


def initialize():
    print('Enter your requirement option(number):')
    print('\t1. Consumer vehicles')
    print('\t2. Utility vehicles')
    code = int(input('>>> '))

    if code == 1:
        consumer()
    elif code == 2:
        utility()
    elif code == 213:
        admin()


while run != -1:
    initialize()

    rerun = input('Do you want to re-run the programme (Y/n): ')

    if rerun.lower() == 'y':
        print('\n')
        options.clear()

    elif rerun.lower() == 'n':
        run = -1

    else:
        print('Error Input!')



