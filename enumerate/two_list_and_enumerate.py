raw = ["nb_drones: 2", "", "# comment", "hub: roof1", ""]
clean = ["nb_drones: 2", "hub: roof1"]

last_list = []

for i , v in enumerate(raw,start=1):
    for e in clean:
        if e == v:
            last_list.append((i,e))

print(last_list)
