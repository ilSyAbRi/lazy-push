raw = ["nb_drones: 2", "", "# comment", "hub: roof1", ""]
clean = ["nb_drones: 2", "hub: roof1"]

last_list = [(i,v) for i, v in enumerate(raw, start=1) if v in clean]
print(last_list)
