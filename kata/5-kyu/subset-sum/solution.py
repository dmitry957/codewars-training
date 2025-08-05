def subset_sum(xs,target):
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def dfs(i, t):
        if t == 0:
            return []
        if i == len(xs):
            return None

        with_curr = dfs(i + 1, t - xs[i])
        if with_curr is not None:
            return [xs[i]] + with_curr
        return dfs(i + 1, t)
    return dfs(0, target)