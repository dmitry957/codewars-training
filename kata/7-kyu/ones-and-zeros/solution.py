def binary_array_to_number(arr):
  return int(f'0b{"".join(map(str, arr))}', 2)