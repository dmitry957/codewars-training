def count_developers(lst):
    return sum(dev["language"]=="JavaScript" and dev["continent"]=="Europe" for dev in lst)