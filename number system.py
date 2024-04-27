# number system
start = int(input("Enter the starting point: "))
end = int(input("Enter the ending point: "))
u = int(input("Enter the updation: "))

rev = input("Do you want to print in reverse order? (yes/no): ").lower()
if (rev == "yes"):
    rev = True
else:
    rev = False

rcv = input("Do you want to print in row-wise or column-wise? (row/column): ").lower()

rowwise = False
if (rcv == "row"):
    rowwise = True

rvo = False
if (rcv == "column"):
    rvo = True

numbers = range(start, end, u) if not rev else range(end, start, -u)

if (rowwise):
    for i in numbers:
        print(i, end=" ")
    print()
else:
    for i in numbers:
        print(i)
