from collections import Counter
names = ["dog","cat","bat","cock","cow","pig","fox",
           "ant","bird","lion","wolf","deer","bear","frog",
           "hen","mole","duck","goat"]
def sc(string):
    char_count = Counter(string)
    animal_counts = [(name, Counter(name)) for name in names]
    def backtrack(available, index=0):
        max_animals = 0
        for i in range(index, len(animal_counts)):
            name, count = animal_counts[i]
            if all(available[c] >= count[c] for c in count):
                new_available = available.copy()
                for c in count:
                    new_available[c] -= count[c]
                max_animals = max(max_animals, 1 + backtrack(new_available, i))
        return max_animals
    return backtrack(char_count)