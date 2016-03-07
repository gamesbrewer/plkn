def bravo_male_dorm_1(camp):
    switcher = {
        "SW": "BL3",
        "SR": "L5A",
        "JP": "BLOK 3",
        "BM": "DURIAN BELANDA L",
        "BS": "WB1",
    }
    return switcher.get(camp, "")

def bravo_male_dorm_2(camp):
    switcher = {
        "SW": "BL4",
        "SR": "L5B",
        "JP": "BLOK 4",
        "BM": "JAMBU MAWAR",
        "BS": "WB2",
    }
    return switcher.get(camp, "")

def bravo_male_dorm_3(camp):
    switcher = {
        "SW": "",
        "SR": "L6A",
        "JP": "",
        "BM": "",
        "BS": "WB3",
    }
    return switcher.get(camp, "")

def bravo_male_dorm_4(camp):
    switcher = {
        "SW": "",
        "SR": "L6B",
        "JP": "",
        "BM": "",
        "BS": "",
    }
    return switcher.get(camp, "")

#----- Female -----------------------

def bravo_female_dorm_1(camp):
    switcher = {
        "SW": "BP5",
        "SR": "P5A",
        "JP": "BLOK 3P",
        "BM": "KELAPA",
        "BS": "WWB1",
    }
    return switcher.get(camp, "")

def bravo_female_dorm_2(camp):
    switcher = {
        "SW": "BP6",
        "SR": "P5B",
        "JP": "BLOK 4P",
        "BM": "LANGSAT",
        "BS": "WWB2",
    }
    return switcher.get(camp, "")

def bravo_female_dorm_3(camp):
    switcher = {
        "SW": "",
        "SR": "P6A",
        "JP": "",
        "BM": "",
        "BS": "WWB3",
    }
    return switcher.get(camp, "")

def bravo_female_dorm_4(camp):
    switcher = {
        "SW": "",
        "SR": "P6B",
        "JP": "",
        "BM": "",
        "BS": "",
    }
    return switcher.get(camp, "")