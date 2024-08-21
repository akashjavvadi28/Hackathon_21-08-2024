import datetime

class ChildVaccinationManagementSystem:
    def __init__(self):
        self.children = {}
        self.vaccination_schedule = {
            "BCG": "At birth",
            "Hepatitis B": "At birth",
            "Polio": "6 weeks",
            "DTP": "6 weeks",
            "MMR": "9 months"
        }
        self.appointments = []

    def validate_date(self, date_str):
        try:
            datetime.datetime.strptime(date_str, '%d-%m-%Y')
            return True
        except ValueError:
            return False

    def add_child(self):
        name = input("Enter child's name: ")
        dob = input("Enter child's date of birth (DD-MM-YYYY): ")
        if not self.validate_date(dob):
            print("Invalid date format. Please use DD-MM-YYYY.")
            return
        parent_contact = input("Enter parent's contact number: ")
        self.children[name] = {'DOB': dob, 'Parent Contact': parent_contact}
        print(f"Child {name} added successfully!")

    def view_vaccination_schedule(self):
        print("\nVaccination Schedule:")
        for vaccine, time in self.vaccination_schedule.items():
            print(f"{vaccine}: {time}")
    
    def book_appointment(self):
        name = input("Enter child's name for the appointment: ")
        if name in self.children:
            vaccine = input("Enter vaccine name: ")
            if vaccine not in self.vaccination_schedule:
                print("Invalid vaccine name. Please check the vaccination schedule.")
                return
            date = input("Enter appointment date (DD-MM-YYYY): ")
            if not self.validate_date(date):
                print("Invalid date format. Please use DD-MM-YYYY.")
                return
            
            # Check for appointment conflicts
            for appointment in self.appointments:
                if appointment['Child'] == name and appointment['Date'] == date:
                    print("An appointment is already booked for this child on this date.")
                    return
            
            self.appointments.append({'Child': name, 'Vaccine': vaccine, 'Date': date})
            print(f"Appointment for {name} booked successfully on {date} for {vaccine}!")
        else:
            print("Child not found in the system. Please add the child first.")
    
    def view_appointments(self):
        print("\nUpcoming Appointments:")
        if not self.appointments:
            print("No upcoming appointments.")
        for appointment in self.appointments:
            print(f"Child: {appointment['Child']}, Vaccine: {appointment['Vaccine']}, Date: {appointment['Date']}")
    
    def send_reminders(self):
        print("\nReminders for Upcoming Appointments:")
        if not self.appointments:
            print("No reminders to send.")
        for appointment in self.appointments:
            print(f"Reminder: {appointment['Child']} has an appointment on {appointment['Date']} for {appointment['Vaccine']}.")

    def update_vaccination_status(self):
        name = input("Enter child's name to update vaccination status: ")
        vaccine = input("Enter vaccine name: ")
        for appointment in self.appointments:
            if appointment['Child'] == name and appointment['Vaccine'] == vaccine:
                self.appointments.remove(appointment)
                print(f"Vaccination status for {name} updated. {vaccine} marked as completed!")
                return
        print("No matching appointment found.")
    
    def search_child(self):
        name = input("Enter child's name to search: ")
        if name in self.children:
            print(f"Child: {name}, DOB: {self.children[name]['DOB']}, Parent Contact: {self.children[name]['Parent Contact']}")
            print("Upcoming Appointments:")
            for appointment in self.appointments:
                if appointment['Child'] == name:
                    print(f"Vaccine: {appointment['Vaccine']}, Date: {appointment['Date']}")
        else:
            print("Child not found in the system.")
    
    def run(self):
        while True:
            print("\nChild Vaccination Management System")
            print("1. Add Child Information")
            print("2. View Vaccination Schedule")
            print("3. Book Vaccination Appointment")
            print("4. View Upcoming Appointments")
            print("5. Send Reminders")
            print("6. Update Vaccination Status")
            print("7. Search Child Information")
            print("8. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_child()
            elif choice == '2':
                self.view_vaccination_schedule()
            elif choice == '3':
                self.book_appointment()
            elif choice == '4':
                self.view_appointments()
            elif choice == '5':
                self.send_reminders()
            elif choice == '6':
                self.update_vaccination_status()
            elif choice == '7':
                self.search_child()
            elif choice == '8':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    system = ChildVaccinationManagementSystem()
    system.run()
