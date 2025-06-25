def bucket_of(said):
    said = said.lower()
    if any(word in said for word in ('water', 'wet', 'wash')) and any(phrase in said for phrase in ('i don\'t know', 'slime')):
        return 'sludge'
    elif any(word in said for word in ('water', 'wet', 'wash')):
        return 'water'
    elif any(phrase in said for phrase in ('i don\'t know', 'slime')):
        return 'slime'
    else: return 'air'