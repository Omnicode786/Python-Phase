# Sample data structure for groups
groups = {
    "sales": ["Alice", "Bob", "Charlie"],
    "engineering": {
        "members": ["Dave", "Eve"],
        "subgroups": {
            "frontend": ["Frank", "Grace"],
            "backend": ["Hank", "Ivy", "Jack"],
            "devops": ["Ken", "Leo", "Mia"]
        }
    },
    "everyone": {
        "members": ["Sales Leader", "Engineering Leader"],
        "subgroups": {
            "sales": ["Alice", "Bob", "Charlie"],
            "engineering": {
                "members": ["Dave", "Eve"],
                "subgroups": {
                    "frontend": ["Frank", "Grace"],
                    "backend": ["Hank", "Ivy", "Jack"],
                    "devops": ["Ken", "Leo", "Mia"]
                }
            }
        }
    }
}

# Function to get members of a group
def get_members(group_name):
    group = groups.get(group_name)
    if isinstance(group, dict):
        # If it's a group with subgroups, return both members and subgroup names
        return group["members"] + list(group["subgroups"].keys())
    elif isinstance(group, list):
        # If it's a list of members (no subgroups), just return the members
        return group
    return []

# Function to check if a member is a group (i.e., a subgroup)
def is_group(member):
    for group in groups.values():
        if isinstance(group, dict) and "subgroups" in group:
            if member in group["subgroups"]:
                return True
    return False

# Recursive count_users function to count users and subgroups


# google below gpt above
def count_users(group_name):
    count = 0
    for member in get_members(group_name):
        count += 1
        if is_group(member):
            count += count_users(member)  - 1 
            # - 1 becauase even though this is a group and not a member it got added once as a memeber above
    return count

# Example calls
print(count_users("sales"))        # Should print 3 (3 members in "sales")
print(count_users("engineering"))  # Should print 8 (5 members + 3 subgroups)
print(count_users("everyone"))     # Should print 18 (18 total users in "everyone" group)
