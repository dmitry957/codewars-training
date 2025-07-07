def get_users_ids(st):
    return [id.strip().lower().removeprefix('uid').strip() for id in st.replace('#', '').split(',')]