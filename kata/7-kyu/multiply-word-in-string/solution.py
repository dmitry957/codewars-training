def modify_multiply(st, loc, num):
    words = st.split()
    return '-'.join([words[loc]] * num)