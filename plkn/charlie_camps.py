def charlie_male_dorm_1(camp):
    switcher = {
        "SW": "BL5",
        "SR": "L7A",
        "JP": "BLOK 5",
        "BM": "MANGGIS",
        "BS": "WC1",
    }
    return switcher.get(camp, "")

def charlie_male_dorm_2(camp):
    switcher = {
        "SW": "BL6",
        "SR": "L7B",
        "JP": "BLOK 6",
        "BM": "NANGKA",
        "BS": "WC2",
    }
    return switcher.get(camp, "")

def charlie_male_dorm_3(camp):
    switcher = {
        "SW": "",
        "SR": "L8A",
        "JP": "",
        "BM": "",
        "BS": "WC3",
    }
    return switcher.get(camp, "")

def charlie_male_dorm_4(camp):
    switcher = {
        "SW": "",
        "SR": "L8B",
        "JP": "",
        "BM": "",
        "BS": "",
    }
    return switcher.get(camp, "")

#----- Female -----------------------

def charlie_female_dorm_1(camp):
    switcher = {
        "SW": "BP3",
        "SR": "P7A",
        "JP": "BLOK 5P",
        "BM": "NENAS",
        "BS": "WWC1",
    }
    return switcher.get(camp, "")

def charlie_female_dorm_2(camp):
    switcher = {
        "SW": "BP6A",
        "SR": "P7B",
        "JP": "BLOK 6P",
        "BM": "BETIK",
        "BS": "WWC2",
    }
    return switcher.get(camp, "")

def charlie_female_dorm_3(camp):
    switcher = {
        "SW": "",
        "SR": "P8A",
        "JP": "",
        "BM": "",
        "BS": "WWC3",
    }
    return switcher.get(camp, "")

def charlie_female_dorm_4(camp):
    switcher = {
        "SW": "",
        "SR": "P8B",
        "JP": "",
        "BM": "",
        "BS": "",
    }
    return switcher.get(camp, "")