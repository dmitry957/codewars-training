def is_flush(cards):
    return len(set([card[-1] for card in cards])) == 1