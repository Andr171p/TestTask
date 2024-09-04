from datetime import datetime


def str_to_timestamp(date: str):
    timestamp = datetime.strptime(
        date,
        '%Y-%m-%d %H:%M:%S'
    ).timestamp()
    return timestamp
