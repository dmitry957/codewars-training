from collections import defaultdict
def type_of_function(domain, codomain, relations):
    mapping = defaultdict(set)
    for x, y in relations:
        if x not in domain or y not in codomain:
            continue
        mapping[x].add(y)
    
    for vals in mapping.values():
        if len(vals) > 1:
            return 'It is not a function'
            
    if set(mapping.keys()) != set(domain):
        return 'It is not a function'
    
    reverse_mapping = defaultdict(set)
    for x, y_set in mapping.items():
        for y in y_set:
            reverse_mapping[y].add(x)
            
    is_injective = all(len(v) == 1 for v in reverse_mapping.values())
    is_surjective = set(reverse_mapping.keys()) == codomain
    
    if is_injective and is_surjective:
        return 'Bijective'
    elif is_injective:
        return 'Injective'
    elif is_surjective:
        return 'Surjective'
    else:
        return 'General function'