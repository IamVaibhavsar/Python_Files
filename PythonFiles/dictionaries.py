monthConversions={
    "Jan":"January",
    "Feb":"February",
    "Dec":"December"
}

print(monthConversions["Feb"])
#OR
print(monthConversions.get("Dec"))

print(monthConversions.get("Love"))
print(monthConversions.get("Love","NOT A VALID KEY"))


