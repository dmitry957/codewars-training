def outed(meet, boss):
    happiness_rating = sum(score * 2 if name == boss else score for name, score in meet.items()) / len(meet)
    return 'Get Out Now!' if happiness_rating <= 5 else 'Nice Work Champ!'