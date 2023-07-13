import random

services = ["component1", "component2", "component3", "component4", "component5", "component6", "component7", "component8"]

table = []

# Extend the table up to app66
for i in range(1, 67):
    app_name = f"app{i:02d}"
    random_services = random.choices(services, k=random.randint(1, len(services)))
    table.append((app_name, random_services))

# Print the table
for app, services in table:
    print(app, services)
