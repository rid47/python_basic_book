class Computer():
    def __init__(self, cpu, ram, mobo):
        self.cpu = cpu
        self.ram = ram
        self.mobo = mobo

    def operation(self):
        print("Can watch movies")
        print("Can play games")
        print("Play Music")
        print("Compute")

    def __str__(self):
        return self.cpu


my_computer = Computer("i3", "4GB", "Esonic")

print(my_computer)

my_computer.operation()

print(my_computer.cpu)
print(my_computer.ram)
print(my_computer.mobo)

my_computer.cpu = "i7"
my_computer.ram = "16GB"
my_computer.mobo = "GIGABYTE"

print(f"After upgradation: {my_computer.cpu}, {my_computer.ram}, {my_computer.mobo}")
