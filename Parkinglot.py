

import Vehicle

# main class


class ParkingLot:

    def __init__(self):
        self.capacity = 0
        self.slotid = 0
        self.numOfOccupiedSlots = 0

# function to create parkinglot

    def createParkingLot(self, capacity):
        self.slots = [-1] * capacity
        self.capacity = capacity
        return print('\nCreated a parking lot with '+str(self.capacity)+' slots') # noqa

# function to create empty slot

    def getEmptySlot(self):
        for i in range(len(self.slots)):
            if self.slots[i] == -1:
                return i

# function to create parking

    def park(self, regno, color):
        if self.numOfOccupiedSlots < self.capacity:
            slotid = self.getEmptySlot()
            self.slots[slotid] = Vehicle.Car(regno, color)
            self.slotid = self.slotid+1
            self.numOfOccupiedSlots = self.numOfOccupiedSlots + 1
            return slotid+1
        else:
            return -1

# function to free parkingslot

    def leave(self, slotid):

        if self.numOfOccupiedSlots > 0 and self.slots[slotid-1] != -1:
            self.slots[slotid-1] = -1
            self.numOfOccupiedSlots = self.numOfOccupiedSlots - 1
            return True
        else:
            return False

# function to check status of parkinglot

    def status(self):
        print("Slot No.\tRegistration No.\tColour")
        for i in range(len(self.slots)):
            if self.slots[i] != -1:
                print(str(i+1) + "\t\t" + str(self.slots[i].regno) + "\t\t" + str(self.slots[i].color)) # noqa
            else:
                continue

# function to get registered number from color

    def getRegNoFromColor(self, color):

        regnos = []
        for i in self.slots:

            if i == -1:
                continue
            if i.color == color:
                regnos.append(i.regno)
        return regnos

# function to get slot number from registerd number

    def getSlotNoFromRegNo(self, regno):

        for i in range(len(self.slots)):
            if self.slots[i].regno == regno:
                return i+1
            else:
                continue
        return -1

# function to get slot number from color

    def getSlotNoFromColor(self, color):

        slotnos = []

        for i in range(len(self.slots)):

            if self.slots[i] == -1:
                continue
            if self.slots[i].color == color:
                slotnos.append(str(i+1))
        return slotnos

# function for display

    def screen(self, line):
        if line.startswith('create_parking_lot'):
            n = int(line.split(' ')[1])
            res = self.createParkingLot(n)
            print('Created a parking lot with '+str(res)+' slots')

        elif line.startswith('park'):
            regno = line.split(' ')[1]
            color = line.split(' ')[2]
            res = self.park(regno, color)
            if res == -1:
                print("Sorry, parking lot is full")
            else:
                print('Allocated slot number: '+str(res))

        elif line.startswith('leave'):
            leave_slotid = int(line.split(' ')[1])
            status = self.leave(leave_slotid)
            if status:
                print('Slot number '+str(leave_slotid)+' is free')

        elif line.startswith('status'):
            self.status()

        elif line.startswith('registration_numbers_for_cars_with_colour'):
            color = line.split(' ')[1]
            regnos = self.getRegNoFromColor(color)
            print(', '.join(regnos))

        elif line.startswith('slot_numbers_for_cars_with_colour'):
            color = line.split(' ')[1]
            slotnos = self.getSlotNoFromColor(color)
            print(', '.join(slotnos))

        elif line.startswith('slot_number_for_registration_number'):
            x = line.split()
            regno = x[1]
            slotno = self.getSlotNoFromRegNo(regno)
            if slotno == -1:
                print("Not found")
            else:
                print(slotno)
        elif line.startswith('exit'):
            exit(0)


if __name__ == '__main__':

    parkinglot = ParkingLot()

    print("Welcome to a Car Parking System")
    entry = int(input("\nEnter 1 for Manual input\nEnter 2 for File input\n"))

# logic for manual input

    if entry == 1:
        n = int(input("Create the total slots available "))
        capacity = parkinglot.createParkingLot(n)

# logic for performing action based on user input
        while True:
            print("\nEnter 1 to park\nEnter 2 to leave the Car on particular slot\nEnter 3 for Status\nEnter 4 for registration numbers for cars with colour\nEnter 5 for slot numbers for cars with colour\nEnter 6 for slot number for registration number\nEnter 7 to Exit") # noqa

            action = int(input())
# for parking
            if action == 1:
                getpark = input("Enter Lisence Number and Color of Car \n").split() # noqa

                parking = parkinglot.park(getpark[0], getpark[1])
                if parking == -1:
                    print("Sorry, parking lot is full")
                else:
                    print('Allocated slot number: '+str(parking))

# for removing

            elif action == 2:
                leave_slotid = int(input("Enter the slot number \n"))
                status = parkinglot.leave(leave_slotid)
                if status:
                    print('Slot number '+str(leave_slotid)+' is free')

# for getting status

            elif action == 3:
                print(parkinglot.status())

# for getting registerd number of car from color

            elif action == 4:
                color = input("Enter the Color of the Car \n")
                regnos = parkinglot.getRegNoFromColor(color)
                print(', '.join(regnos))

# for getting slot number of car from color

            elif action == 5:
                color = input("Enter the Color of the Car \n")
                slotnos = parkinglot.getSlotNoFromColor(color)
                print(', '.join(slotnos))

# for getting slot number from registerd number

            elif action == 6:
                regno = input("Enter the Registration number of the Car \n")
                slotno = parkinglot.getSlotNoFromRegNo(regno)
                if slotno == -1:
                    print("Slot number doesnot found for the Car ")
                else:
                    print(slotno)

# to exit

            elif action == 7:
                break

# textfile as input

    elif entry == 2:
        getentry = input("Enter your file name\n")
        with open(getentry) as f:
            for line in f:
                parkinglot.screen(line)
