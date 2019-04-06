from kata.name_list import namelist

def test_bart_lisa_maggie():
    names = [
        {"name": "Bart"},
        {"name": "Lisa"},
        {"name": "Maggie"}
    ]
    expected = "Bart, Lisa & Maggie"
    assert expected == namelist(names)

def test_empty_string():
    names = [{"name": ""}]
    expected = ""
    assert expected == namelist(names)

def test_single_name():
    names = [{"name": "Bart"}]
    expected = "Bart"
    assert expected == namelist(names)

def test_two_names():
    names = [{"name": "Bart"}, {"name": "Lisa"}]
    expected = "Bart & Lisa"
    assert expected == namelist(names)
