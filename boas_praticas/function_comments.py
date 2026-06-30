def get_name(fullname: str) -> str:
    """
    Extracts the name of the file by splitting using anderscore '_' and returning the first part.

    [input]
        >> fullname: example: "Fred_Santos"
    [output]
        >> name: example: "Fred"
    """
    name, *_ = fullname.split("_")
    return name

print(get_name("Fred_Santos"))  # Output: Fred
