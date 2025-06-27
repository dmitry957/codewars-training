def work_needed(project_minutes, free_lancers):
    total_freelancer_minutes = sum(h * 60 + m for h, m in free_lancers)
    if project_minutes <= total_freelancer_minutes:
        return 'Easy Money!'
    
    remaining_minutes = project_minutes - total_freelancer_minutes
    hours = remaining_minutes // 60
    minutes = remaining_minutes % 60
    return f'I need to work {hours} hour(s) and {minutes} minute(s)'