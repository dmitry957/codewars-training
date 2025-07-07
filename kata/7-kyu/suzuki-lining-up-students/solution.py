def lineup_students(st):
    st = st.split()
    return sorted(st, key = lambda x: (len(x), x), reverse = True)