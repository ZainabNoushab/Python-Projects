import csv
from datetime import date
import os

TRACKER_FILE = 'tracker.csv'

def create_tracker():
    print("\nLet's Create a Tracker!")
    fields_input = input("Enter the fields for your tracker, separated by commas: ")
    headers = ["Date"] + [field.strip() for field in fields_input.split(',')]

    with open(TRACKER_FILE, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)

    print("Tracker created successfully!")
    return headers

# function to load tracker headers
def load_headers():
    if not os.path.exists(TRACKER_FILE):
        return create_tracker()
    
    with open(TRACKER_FILE, mode='r') as f:
        reader = csv.reader(f)
        headers = next(reader)
    
    return headers

#function to log a daily entry
def log_entry(headers):
    print(f"\nLogging for {date.today()}")
    entry = [str(date.today())]

    for field in headers[1:]:
        value = input(f"{field}: ")
        entry.append(value)

    with open(TRACKER_FILE, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(entry)

    print("Entry logged successfully!")

def view_entries():
    if not os.path.exists(TRACKER_FILE):
        print("No tracker file found. Please create a tracker first.")
        return

    with open(TRACKER_FILE, mode='r') as f:
        reader =csv.reader(f)
        for row in reader:
            print(' | '.join(row))

# add new fields in the tracker
def add_fields():
    if not os.path.exists(TRACKER_FILE):
        print("No tracker file found. Please create a tracker first.")
        return

    new_fields = input("Enter new fields to add, separated by commas: ")
    new_fields = [field.strip() for field in new_fields.split(',')]

    with open(TRACKER_FILE, mode='r', newline='') as f:
        reader = list(csv.reader(f))
        headers = reader[0]
        rows = reader[1:]
    
    # add new headers
    updated_headers = headers + new_fields
    
    for row in rows:
        row += [''] * len(new_fields)

    with open(TRACKER_FILE, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(updated_headers)
        writer.writerows(rows)

    print("New fields added successfully!")
    return updated_headers

#main function
def main():
    print("\nWelcome to daily tracker!")
    headers = load_headers()

    if not headers:
        user_choice = input("No tracker found. Would you like to create one? (yes/no): ").strip().lower()
        if user_choice == 'yes':
            headers = create_tracker()
        else:
            print("Exiting the tracker. Goodbye!")
            return
        
    while True:
        print("\nMain Menu")
        print("1. Log today's entry")
        print("2. View past entries")
        print("3. Reset tracker")
        print("4. Add new fields to tracker")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            log_entry(headers)
        elif choice == '2':
            view_entries()
        elif choice == '3':
            confirm = input("This will delete all data. Type 'yes' to confirm: ").lower()
            if confirm == "yes":
                os.remove(TRACKER_FILE)
                print("🗑️ Tracker reset. Please restart to create a new one.")
                break
        elif choice == '4':
            headers = add_fields()
            if headers:
                print("Fields updated successfully!")
        elif choice == '5':
            print("Goodbye!")
            break
        
if __name__ == "__main__":
    main()