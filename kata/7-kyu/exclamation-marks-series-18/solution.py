def slot(st):
    if st == '!' * 5 or st == '?' * 5:
        return 1000
    elif '!' * 4 in st or '?' * 4 in st:
        return 800
    elif ('!' * 3 in st and '?' * 2 in st) or ('?' * 3 in st and '!' * 2 in st):
        return 500
    elif ('!' * 3 in st and not '?' * 2 in st) or ('?' * 3 in st and not '!' * 2 in st):
        return 300
    elif st in ('??!??', '!!??!', '!!?!!', '!??!!', '??!!?', '?!!??'):
        return 200
    elif (st.count('!!') == 1 and st.count('??') == 0) or (st.count('!!') == 0 and st.count('??') == 1):
        return 100
    else: return 0