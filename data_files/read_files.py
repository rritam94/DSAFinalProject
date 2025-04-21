import csv
def read_fruit_prices():
    filePath = "data_files/Fruit-Prices-2022.csv"
    pricelst = []


    with open(filePath, mode='r') as file:# Open and read the CSV file
        reader = csv.reader(file)

        next(reader) # Skip the header row

        # Process each row and extract fruit name and retail price per pound
        for row in reader:
            fruit = row[0]
            price = int((float(row[2]) + .005) * 100)  # Convert prices to cents
            pricelst.append((fruit, price))  # Create tuple and add to list

    return pricelst