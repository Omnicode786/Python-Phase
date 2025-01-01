
def invertfunc(resource_dict):
    newdict = {}
    for items, resources in resource_dict.items():
        for resource in resources:
            if resource in newdict:
                newdict[resource].append(items)
            else:
                newdict[resource] = [items]
    return newdict





resource_dict = {"Hard Drives": ["IDE HDDs", "SCSI HDDs"],
        "PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}


print(invertfunc(resource_dict))
