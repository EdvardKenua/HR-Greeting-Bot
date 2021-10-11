def getName(full_name):
    sym = full_name.index("#")
    name = full_name
    name = list(full_name)
    name[sym] = "-"
    name = "".join(name)
    return name
