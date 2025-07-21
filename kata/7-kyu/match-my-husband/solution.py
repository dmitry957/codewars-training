def match(usefulness, months):
    rating = round(100 * (1 - 0.15) ** months, 4)
    return "Match!" if sum(usefulness) >= rating else "No match!"