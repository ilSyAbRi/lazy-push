lines = ["nb_drones: 2", "", "# comment", "hub: roof1", ""]

for i , v in enumerate(lines, start=1):
    if v and not v.startswith("#"):
        print(i, v)
