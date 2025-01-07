import csv

# Load train data from Train.csv
def load_train_data(train_file):
    trains = {}
    with open(train_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            train_id = row["trainId"]
            trains[train_id] = {
                "train name": row["train name"],
                "source station": row["source station"],
                "destination station": row["destination station"],
                "total seats": int(row["total seats"]),
                "available seats": int(row["total seats"]),
                "revenue": 0
            }
    return trains

# Load passenger data from passengers.csv
def load_passenger_data(passenger_file):
    passengers = []
    with open(passenger_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            passengers.append({
                "passenger name": row["passenger name"],
                "trainID": row["trainID"],
                "number of tickets": int(row["number of tickets"])
            })
    return passengers

# Check seat availability
def check_seat_availability(trains, train_id, num_tickets):
    if train_id in trains:
        return trains[train_id]["available seats"] >= num_tickets
    return False

# Confirm booking and calculate fare
def confirm_booking(trains, passengers):
    fare_per_ticket = 500  # Example fare price per ticket
    confirmed_bookings = []
    
    for passenger in passengers:
        train_id = passenger["trainID"]
        num_tickets = passenger["number of tickets"]
        
        if check_seat_availability(trains, train_id, num_tickets):
            trains[train_id]["available seats"] -= num_tickets
            total_fare = num_tickets * fare_per_ticket
            trains[train_id]["revenue"] += total_fare
            confirmed_bookings.append({
                "passenger name": passenger["passenger name"],
                "trainID": train_id,
                "number of tickets": num_tickets,
                "total fare": total_fare
            })
    
    return confirmed_bookings

# Generate reports
def generate_reports(trains):
    report1 = "Train Details Report\n"
    report1 += "Train ID, Train Name, Source Station, Destination Station, Total Seats, Available Seats\n"
    for train_id, train in trains.items():
        report1 += f"{train_id}, {train['train name']}, {train['source station']}, {train['destination station']}, {train['total seats']}, {train['available seats']}\n"
    
    report2 = "Revenue Report\n"
    report2 += "Train ID, Train Name, Total Revenue\n"
    for train_id, train in trains.items():
        report2 += f"{train_id}, {train['train name']}, {train['revenue']}\n"
    
    return report1, report2

# Main function
def main():
    train_file = 'Train.csv'
    passenger_file = 'passengers.csv'
    
    trains = load_train_data(train_file)
    passengers = load_passenger_data(passenger_file)
    
    confirmed_bookings = confirm_booking(trains, passengers)
    
    report1, report2 = generate_reports(trains)
    
    print(report1)
    print(report2)

if __name__ == "__main__":
    main()
