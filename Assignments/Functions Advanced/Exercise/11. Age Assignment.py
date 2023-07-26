def age_assignment(*args, **kwargs):
    res = {}

    for el in args:
        key = el[0]
        res[el] = kwargs[key]

    return res


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
