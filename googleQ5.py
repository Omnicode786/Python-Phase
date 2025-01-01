#same Q as Q4


def fullnamefunc(empnames):
    fullnames = []
    for lastname, firstnames in empnames.items():
        for firstname in firstnames:
            fullnames.append(firstname + " " + lastname)
    return " ".join(fullnames)



empnames = {
    "Ali": ["Muhammad", "Ahmed", "Haider"], "Alam":["Mansoor", "Muzammil", "Hamida"], "Khan":["Shehriyar", "Hamza", "Murtaza"]
}

print(fullnamefunc(empnames))