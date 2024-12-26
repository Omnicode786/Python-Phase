teams = ["Pakistan", "India", "England", "Australia"]
for home in teams:
    for away in teams:
        if home != away:
            print(home + " vs " + away)
