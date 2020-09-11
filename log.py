from decimal import Decimal

def main():

    with open('C:\\Users\\xxx\\AppData\\Roaming\\FAHClient\\log.txt', "r") as inputFile:
        lines = inputFile.readlines()

    print("")
    print("Found the following credits:")
    print("----------------------------")

    finalCount = 0
    totalCredits = 0
    sendingCount = 0

    for line in lines:
        if "Final" in line:
            finalCount += 1
            totalCredits += Decimal(line.split(" ")[3])
            print(line.strip("\n"))
        if "Sending" in line:
            sendingCount += 1

    print("")
    print("----------------------------")
    print(f"Final Count: {finalCount}")
    print(f"Sending Count: {sendingCount}")
    print(f"Total Credits: {totalCredits}")


if __name__ == "__main__":
    main()