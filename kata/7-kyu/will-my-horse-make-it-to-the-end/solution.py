def estimator(obstacles, stamina):
    obstacle_count = 0
    for o in obstacles:
        if o == 1:
            obstacle_count += 1
        elif o == 0:
            stamina -= get_obstacle_penalty(obstacle_count)
            obstacle_count = 0
    if obstacle_count > 0:
        stamina -= get_obstacle_penalty(obstacle_count)
    return stamina >= 0

def get_obstacle_penalty(count):
    return {1: 2, 2: 5, 3: 10}.get(count, 0)