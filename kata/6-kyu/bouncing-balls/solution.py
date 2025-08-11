def bouncing_ball(h, bounce, window):
    if h>0 and 0 < bounce < 1 and window < h:
        count = 1
        h*= bounce
        while h > window:
            count+=2
            h*=bounce
        return count
    return -1