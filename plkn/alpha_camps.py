def alpha_male_dorm_1(camp):
    switcher = {
        "SW": "BL1",
        "SR": "L3A",
        "JP": "BLOK 1",
        "BM": "BACANG",
        "BS": "WA1",
    }
    return switcher.get(camp, "")

def alpha_male_dorm_2(camp):
    switcher = {
        "SW": "BL2",
        "SR": "L3B",
        "JP": "BLOK 2",
        "BM": "CIKU",
        "BS": "WA2",
    }
    return switcher.get(camp, "")

def alpha_male_dorm_3(camp):
    switcher = {
        "SW": "",
        "SR": "L4A",
        "JP": "",
        "BM": "",
        "BS": "WA3",
    }
    return switcher.get(camp, "")

def alpha_male_dorm_4(camp):
    switcher = {
        "SW": "",
        "SR": "L4B",
        "JP": "",
        "BM": "",
        "BS": "",
    }
    return switcher.get(camp, "")

#----- Female -----------------------

def alpha_female_dorm_1(camp):
    switcher = {
        "SW": "BP7",
        "SR": "P3A",
        "JP": "BLOK 1P",
        "BM": "CEMPEDAK",
        "BS": "WWA1",
    }
    return switcher.get(camp, "")

def alpha_female_dorm_2(camp):
    switcher = {
        "SW": "BP8",
        "SR": "P3B",
        "JP": "BLOK 1P",
        "BM": "MATA KUCING",
        "BS": "WWA2",
    }
    return switcher.get(camp, "")

def alpha_female_dorm_3(camp):
    switcher = {
        "SW": "",
        "SR": "P4A",
        "JP": "",
        "BM": "",
        "BS": "WWA3",
    }
    return switcher.get(camp, "")

def alpha_female_dorm_4(camp):
    switcher = {
        "SW": "",
        "SR": "P4B",
        "JP": "",
        "BM": "",
        "BS": "",
    }
    return switcher.get(camp, "")