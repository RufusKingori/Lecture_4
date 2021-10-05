#This program converts date formats

def main():

    dateStr = input("Enter a date (mm/dd/yyyy): ")
    monthStr, dayStr, yearStr = dateStr.split("/")

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    for i in (months):
        monthStr = months[i+1]
    print("The converted date is:", monthStr, dayStr + ",", yearStr)

main()

