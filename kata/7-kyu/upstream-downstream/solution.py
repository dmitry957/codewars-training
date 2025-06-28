def time(distance,boat_speed,stream):
    streamline, stream_speed = stream.split()
    stream_speed = int(stream_speed) if streamline == 'Downstream' else -(int(stream_speed))
    return round(distance / (boat_speed + stream_speed), 2)