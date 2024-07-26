# Retourner une Exception custom


class MonException(Exception):
    pass


def foo(name: str):
    if name == "Patrick":
        raise MonException("Exception personnalisée")
    return name


print(foo("Patrick"))
