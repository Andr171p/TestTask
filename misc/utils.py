from datetime import datetime


def str_to_timestamp(date: str):
    timestamp = datetime.strptime(
        date,
        '%Y-%m-%d %H:%M:%S'
    ).timestamp()
    return timestamp


print(str_to_timestamp(date='2008-11-26 15:47:01'))
