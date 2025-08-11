def like_or_dislike(lst):
    result = 'Nothing'
    for reaction in lst:
        result = reaction if result != reaction else 'Nothing'
    return result