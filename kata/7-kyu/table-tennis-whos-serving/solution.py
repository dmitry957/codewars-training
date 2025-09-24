def who_is_serving(current_round: int) -> int:
    return 1 if (current_round // 2) % 2 == 0 else 2