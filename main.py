def sozlar_chastotasi(matn):
    matn = matn.lower()  # katta-kichik harflarni farqlamaymiz
    sozlar = matn.split()  # sozlar ro'yxatiga aylanadi
    chastotalar = {}  # sozlar chastotasi lug'atiga aylanadi

    for soz in sozlar:
        if soz in chastotalar:
            chastotalar[soz] += 1
        else:
            chastotalar[soz] = 1

    return chastotalar

matn = "Hello world hello"
print(sozlar_chastotasi(matn))  # {'hello': 2, 'world': 1}
