time = int(input())

hours = time // 100
minutes = time % 100

total = hours * 60 + minutes

offsets = {
    "Ottawa": 0,
    "Victoria": -180,
    "Edmonton": -120,  
    "Winnipeg": -60,    
    "Toronto": 0, 
    "Halifax": 60,
    "St. John's": 90
}

for city, offset in offsets.items():
    local = (total + offset) % (24 * 60)
    local_hour = local // 60
    local_min = local % 60
    print(f"{local_hour * 100 + local_min} in {city}")