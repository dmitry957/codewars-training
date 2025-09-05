def archers_ready(archers):
    if not len(archers):
        return False
    return all(arrows >= 5 for arrows in archers)