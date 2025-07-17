def reject(seq, predicate):
    return [i for i in seq if i not in filter(predicate,seq)]