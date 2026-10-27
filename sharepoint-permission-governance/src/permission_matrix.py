def validate_matrix(matrix):
    required_groups = {"Northstar Owners", "Northstar Members", "Northstar Visitors", "HR Records"}
    required_boundaries = {"Shared Guidance", "HR Records"}
    if set(matrix) != required_groups:
        return False, "group coverage is incomplete"
    for group, boundaries in matrix.items():
        if set(boundaries) != required_boundaries:
            return False, f"boundary coverage is incomplete for {group}"
    if matrix["Northstar Members"]["HR Records"] != "No access":
        return False, "restricted boundary still inherits member access"
    if matrix["HR Records"]["HR Records"] != "Edit":
        return False, "restricted group lacks Edit access"
    return True, "matrix is valid"


matrix = {
    "Northstar Owners": {"Shared Guidance": "Full Control", "HR Records": "Full Control"},
    "Northstar Members": {"Shared Guidance": "Edit", "HR Records": "No access"},
    "Northstar Visitors": {"Shared Guidance": "Read", "HR Records": "No access"},
    "HR Records": {"Shared Guidance": "No access", "HR Records": "Edit"},
}

valid, message = validate_matrix(matrix)
print(message)
