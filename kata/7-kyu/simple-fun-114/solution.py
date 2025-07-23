def abacaba(k):
  return chr(len(bin((k^(k-1)))[2:]) + 96)