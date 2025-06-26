def travel(total_time, run_time, rest_time, speed):
    times = total_time // (run_time + rest_time)
    remaining_time = total_time % (run_time + rest_time)
    final_run_time = min(remaining_time, run_time)
    return speed * (times * run_time + final_run_time)