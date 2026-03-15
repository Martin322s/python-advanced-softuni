def list_roman_emperors(*args, **kwargs):
    success_emperors = {}
    failed_emperors = {}
    result = ""

    for emp_name, status in args:
        if status:
            success_emperors[emp_name] = kwargs.get(emp_name)
        else:
            failed_emperors[emp_name] = kwargs.get(emp_name)

    sorted_success_emperors = sorted(success_emperors.items(), key=lambda kvp: (-kvp[1], kvp[0]))
    sorted_failed_emperors = sorted(failed_emperors.items(), key=lambda kvp: (kvp[1], kvp[0]))

    result = f"Total number of emperors: {len(args)}"

    if success_emperors:
        result += "\nSuccessful emperors:"

        for emp_name, years in sorted_success_emperors:
            result += f"\n****{emp_name}: {years}"

    if failed_emperors:
        result += "\nUnsuccessful emperors:"

        for emp_name, years in sorted_failed_emperors:
            result += f"\n****{emp_name}: {years}"

    return result