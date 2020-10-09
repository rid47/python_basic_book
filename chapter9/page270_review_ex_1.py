captains = {}

captains["Enterprise"] = "Picard"
captains["Voyager"] = "Janeway"
captains["Defiant"] = "Sisko"

print(captains)

if "Enterprise" in captains:
    pass
else:
    captains["Enterprise"] = "unknown"


if "Discovery" in captains:
    pass
else:
    captains["Discovery"] = "unknown"


for key, value in captains.items():
    print(f"The {key} is captained by {value}.")


del captains["Discovery"]
