def team_lineup(*args):
    countries = {}

    for name, country in args:
        if country not in countries:
            countries[country] = []
        countries[country].append(name)

    sorted_countries = sorted(
        countries.items(),
        key=lambda kvp: (-len(kvp[1]), kvp[0])
    )

    result = ""

    for country, players in sorted_countries:
        result += f"{country}:\n"
        for player in players:
            result += f"  -{player}\n"

    return result.rstrip()