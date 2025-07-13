class List:
    def remove_(self, integer_list, values_list):
        remove_set = set(values_list)
        return [item for item in integer_list if item not in remove_set]