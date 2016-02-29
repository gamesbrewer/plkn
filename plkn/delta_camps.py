def delta_male_dorm_1(camp):
    switcher = {
        "SW": "BL7",
        "SR": "L9A",
        "JP": "BLOK 7",
        "BM": "TEMBIKAI",
        "BS": "WD1",
    }
    return switcher.get(camp, "")

def delta_male_dorm_2(camp):
    switcher = {
        "SW": "BL8",
        "SR": "L9B",
        "JP": "BLOK 8",
        "BM": "PULASAN",
        "BS": "WD2",
    }
    return switcher.get(camp, "")

def delta_male_dorm_3(camp):
    switcher = {
        "SW": "",
        "SR": "L10A",
        "JP": "",
        "BM": "",
        "BS": "WD3",
    }
    return switcher.get(camp, "")

def delta_male_dorm_4(camp):
    switcher = {
        "SW": "",
        "SR": "L10B",
        "JP": "",
        "BM": "",
        "BS": "",
    }
    return switcher.get(camp, "")

#----- Female -----------------------

def delta_female_dorm_1(camp):
    switcher = {
        "SW": "BP2",
        "SR": "P9A",
        "JP": "BLOK 7P",
        "BM": "JAMBU BATU",
        "BS": "WWD1",
    }
    return switcher.get(camp, "")

def delta_female_dorm_2(camp):
    switcher = {
        "SW": "BP5A",
        "SR": "P9B",
        "JP": "BLOK 8P",
        "BM": "DURIAN BELANDA p",
        "BS": "WWD2",
    }
    return switcher.get(camp, "")

def delta_female_dorm_3(camp):
    switcher = {
        "SW": "",
        "SR": "P10A",
        "JP": "",
        "BM": "",
        "BS": "WWD3",
    }
    return switcher.get(camp, "")

def delta_female_dorm_4(camp):
    switcher = {
        "SW": "",
        "SR": "P10B",
        "JP": "",
        "BM": "",
        "BS": "",
    }
    return switcher.get(camp, "")