def get_weekday(current_weekday: int, days_ahead: int)->int:
    return (current_weekday+days_ahead-1) % 7+1

