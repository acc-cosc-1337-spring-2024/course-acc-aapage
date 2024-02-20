def get_hour(epoch_seconds):
    hour = int((epoch_seconds / 3600) % 24)
    return hour

def get_minutes(epoch_seconds):
    minutes = int((epoch_seconds / 60) % 60)
    return minutes

def get_seconds(epoch_seconds):
    seconds = int((epoch_seconds % 3600) % 60)
    return seconds