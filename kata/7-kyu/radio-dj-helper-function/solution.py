def longest_possible(playback):
    def to_seconds(time_str):
        minutes, seconds = list(map(int, time_str.split(':')))
        return minutes * 60 + seconds
    
    longest_duration = -1
    longest_title = False
    for song in songs:
        duration = to_seconds(song['playback'])
        if duration <= playback and duration > longest_duration:
            longest_duration = duration
            longest_title = song['title']
    return longest_title