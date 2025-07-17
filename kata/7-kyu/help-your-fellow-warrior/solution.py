def get_honor_path(honor_score, target_honor_score):
    if target_honor_score <= honor_score:
        return {}
    katas_to_solve = target_honor_score - honor_score
    return {'2kyus': katas_to_solve % 2, '1kyus': katas_to_solve // 2 }