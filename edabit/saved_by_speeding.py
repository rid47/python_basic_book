def time_saved(s_lim, s_avg, d):
    duration_for_speed_limit = d/s_lim
    duration_for_speed_avg = d/s_avg
    return round(((duration_for_speed_limit - duration_for_speed_avg) * 60), 1)


print(time_saved(80, 90, 40))
