import heapq

def closure_gen(*s):
    s = set(s)
    if not s:
        return
    seen = set()
    heap = list(s)
    heapq.heapify(heap)
    while heap:
        val = heapq.heappop(heap)
        if val in seen:
            continue
        seen.add(val)
        yield val
        for x in s:
            product = val * x
            if product not in seen:
                heapq.heappush(heap, product)