#1
objects = [
    ("Containment Cell A", 4),
    ("Archive Vault", 1),
    ("Bio Lab Sector", 3),
    ("Observation Wing", 2)
]
sorted_objects = sorted(objects, key=lambda x: x[1])
for obj in sorted_objects:
    print(f"{obj[0]} - Уровень угрозы: {obj[1]}")

#2
staff_shifts = [
    {"name": "Dr. Shaw", "shift_cost": 120, "shifts": 15},
    {"name": "Agent Torres", "shift_cost": 90, "shifts": 22},
    {"name": "Researcher Hall", "shift_cost": 150, "shifts": 10}
]
total_costs = list(map(lambda emp: emp["shift_cost"] * emp["shifts"], staff_shifts))

print("Общая стоимость работы каждого сотрудника:")
for emp, cost in zip(staff_shifts, total_costs):
    print(f"{emp['name']}: {cost}")
max_cost = max(total_costs)
print(f"\nМаксимальная стоимость работы: {max_cost}")

#3
personnel = [
    {"name": "Dr. Klein", "clearance": 2},
    {"name": "Agent Brooks", "clearance": 4},
    {"name": "Technician Reed", "clearance": 1}
]
personnel_with_category = list(map(
    lambda emp: {
        "name": emp["name"],
        "clearance": emp["clearance"],
        "category": "Top Secret" if emp["clearance"] >= 4
                    else "Confidential" if emp["clearance"] >= 2
                    else "Restricted"
    },
    personnel
))
for emp in personnel_with_category:
    print(f"{emp['name']}: Уровень {emp['clearance']} - {emp['category']}")

#4
zones = [
    {"zone": "Sector-12", "active_from": 8, "active_to": 18},
    {"zone": "Deep Storage", "active_from": 0, "active_to": 24},
    {"zone": "Research Wing", "active_from": 9, "active_to": 17}
]
daytime_zones = list(filter(
    lambda zone: zone["active_from"] >= 8 and zone["active_to"] <= 18,
    zones
))
print("Зоны, работающие полностью в дневной период (8-18):")
for zone in daytime_zones:
    print(f"{zone['zone']}: с {zone['active_from']}:00 до {zone['active_to']}:00")

#5
reports = [
    {"author": "Dr. Moss", "text": "Analysis completed. Reference: http://external-archive.net"},
    {"author": "Agent Lee", "text": "Incident resolved without escalation."},
    {"author": "Dr. Patel", "text": "Supplementary data available at https://secure-research.org"},
    {"author": "Supervisor Kane", "text": "No anomalies detected during inspection."},
    {"author": "Researcher Bloom", "text": "Extended observations uploaded to http://research-notes.lab"},
    {"author": "Agent Novak", "text": "Perimeter secured. No external interference observed."},
    {"author": "Dr. Hargreeve", "text": "Full containment log stored at https://internal-db.scp"},
    {"author": "Technician Moore", "text": "Routine maintenance completed successfully."},
    {"author": "Dr. Alvarez", "text": "Cross-reference materials: http://crosslink.foundation"},
    {"author": "Security Officer Tan", "text": "Shift completed without incidents."},
    {"author": "Analyst Wright", "text": "Statistical model published at https://analysis-hub.org"},
    {"author": "Dr. Kowalski", "text": "Behavioral deviations documented internally."},
    {"author": "Agent Fischer", "text": "Additional footage archived: http://video-storage.sec"},
    {"author": "Senior Researcher Hall", "text": "All test results verified and approved."},
    {"author": "Operations Lead Grant", "text": "Emergency protocol draft shared via https://ops-share.scp"}
]
reports_with_links = list(filter(
    lambda report: 'http://' in report['text'] or 'https://' in report['text'],
    reports
))
print("1. Отчеты, содержащие ссылки:")
for report in reports_with_links:
    print(f"{report['author']}: {report['text']}")
import re
def remove_links(text):
    return re.sub(r'https?://[^\s]+', '[ДАННЫЕ УДАЛЕНЫ]', text)
cleaned_reports = list(map(
    lambda report: {
        "author": report["author"],
        "text": remove_links(report["text"])
    },
    reports_with_links
))
print("\n2. Отчеты после удаления ссылок:")
for report in cleaned_reports:
    print(f"{report['author']}: {report['text']}")
all_cleaned_reports = list(map(
    lambda report: {
        "author": report["author"],
        "text": remove_links(report["text"])
    },
    reports
))
print("\n3. Все отчеты после обработки (включая те, что без ссылок):")
for report in all_cleaned_reports:
    print(f"{report['author']}: {report['text']}")

#6
scp_objects = [
    {"scp": "SCP-096", "class": "Euclid"},
    {"scp": "SCP-173", "class": "Euclid"},
    {"scp": "SCP-055", "class": "Keter"},
    {"scp": "SCP-999", "class": "Safe"},
    {"scp": "SCP-3001", "class": "Keter"}
]
enhanced_containment_scp = list(filter(
    lambda obj: obj["class"] != "Safe",
    scp_objects
))
print("SCP-объекты, требующие усиленных мер содержания:")
for obj in enhanced_containment_scp:
    print(f"{obj['scp']} - Класс: {obj['class']}")
print(f"\nТип результата: {type(enhanced_containment_scp)}")
print(f"Формат элементов: {enhanced_containment_scp[0] if enhanced_containment_scp else 'Список пуст'}")

#7
incidents = [
    {"id": 101, "staff": 4},
    {"id": 102, "staff": 12},
    {"id": 103, "staff": 7},
    {"id": 104, "staff": 20}
]
sorted_incidents = sorted(incidents, key=lambda x: x["staff"], reverse=True)

print("1. Все инциденты, отсортированные по количеству персонала (по убыванию):")
for incident in sorted_incidents:
    print(f"Инцидент {incident['id']}: {incident['staff']} человек")
top_three = sorted_incidents[:3]

print("\n2. Три наиболее ресурсоемких инцидента:")
for incident in top_three:
    print(f"Инцидент {incident['id']}: {incident['staff']} человек")

#8
protocols = [
    ("Lockdown", 5),
    ("Evacuation", 4),
    ("Data Wipe", 3),
    ("Routine Scan", 1)
]
formatted_protocols = list(map(
    lambda protocol: f"Protocol {protocol[0]} - Criticality {protocol[1]}",
    protocols
))
print("Форматированный список протоколов:")
for protocol in formatted_protocols:
    print(protocol)

#9
shifts = [6, 12, 8, 24, 10, 4]
filtered_shifts = list(filter(
    lambda duration: 8 <= duration <= 12,
    shifts
))
print("Смены, длящиеся от 8 до 12 часов включительно:")
for i, shift in enumerate(filtered_shifts, 1):
    print(f"{i}. {shift} часов")

print(f"\nВсего подходящих смен: {len(filtered_shifts)}")

#10
evaluations = [
    {"name": "Agent Cole", "score": 78},
    {"name": "Dr. Weiss", "score": 92},
    {"name": "Technician Moore", "score": 61},
    {"name": "Researcher Lin", "score": 88}
]
best_employee = max(evaluations, key=lambda emp: emp["score"])
print(f"Сотрудник с наивысшей оценкой: {best_employee['name']} - {best_employee['score']} баллов")










































