def namelist(names) -> str:
    """
    Given [{"name": "Bart"}, {"name": "Lisa"}, "name": "Maggie"}]
    Returns "Bart, Lisa & Maggie"
    """
    try:
        if len(names) == 1:
            result = names[0]["name"]
        else:
            result = ", ".join([name["name"] for name in names[:-1]])
            result += " & " + names[-1]["name"]
    except:
        result = ""
    finally:
        return result

