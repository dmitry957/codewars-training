from collections import Counter

class List(object):
    def count_spec_digits(self, integers_list, digits_list):
        all_digits = []
        def get_digits(n):
            n = abs(n)
            result = []
            while n:
                result.append(n%10)
                n //= 10
            return list(reversed(result))
        for n in integers_list:
            all_digits.extend(get_digits(n))
        counter = Counter(all_digits)
        return [(digit, counter[digit]) for digit in digits_list]