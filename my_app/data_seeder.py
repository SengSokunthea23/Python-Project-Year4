from my_app.models import Position, Staff
from datetime import date

# Create Positions first (since Staff references Position)
positions_data = [
    "Manager",
    "Developer", 
    "Designer",
    "Analyst",
    "HR Specialist",
    "Marketing Specialist"
]

print("Creating Positions...")
for pos_name in positions_data:
    position, created = Position.objects.get_or_create(position_name=pos_name)
    if created:
        print(f"Created position: {pos_name}")
    else:
        print(f"Position already exists: {pos_name}")

# Create Staff
staff_data = [
    {
        'last_name': 'Smith',
        'first_name': 'John',
        'gender': 'M',
        'date_of_birth': date(1985, 3, 15),
        'position_name': 'Manager'
    },
    {
        'last_name': 'Johnson',
        'first_name': 'Sarah',
        'gender': 'F',
        'date_of_birth': date(1990, 7, 22),
        'position_name': 'Developer'
    },
    {
        'last_name': 'Williams',
        'first_name': 'Mike',
        'gender': 'M',
        'date_of_birth': date(1988, 11, 8),
        'position_name': 'Designer'
    },
    {
        'last_name': 'Brown',
        'first_name': 'Lisa',
        'gender': 'F',
        'date_of_birth': date(1992, 4, 30),
        'position_name': 'Analyst'
    },
    {
        'last_name': 'Davis',
        'first_name': 'Robert',
        'gender': 'M',
        'date_of_birth': date(1987, 9, 12),
        'position_name': 'HR Specialist'
    }
]

print("\nCreating Staff...")
for staff_info in staff_data:
    position = Position.objects.get(position_name=staff_info['position_name'])
    staff, created = Staff.objects.get_or_create(
        last_name=staff_info['last_name'],
        first_name=staff_info['first_name'],
        defaults={
            'gender': staff_info['gender'],
            'date_of_birth': staff_info['date_of_birth'],
            'position': position
        }
    )
    if created:
        print(f"Created staff: {staff.full_name} - {position.position_name}")
    else:
        print(f"Staff already exists: {staff.full_name}")

print(f"\nTotal Positions: {Position.objects.count()}")
print(f"Total Staff: {Staff.objects.count()}")

# Display all staff with their positions
print(f"\nAll Staff with Positions:")
for staff in Staff.objects.select_related('position').all():
    print(f"ID: {staff.id}, Name: {staff.full_name}, Gender: {staff.gender}, DOB: {staff.date_of_birth}, Position: {staff.position.position_name}")