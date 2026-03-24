def mean(data):
    if len(data) == 0:
        raise ValueError("Mean is undefined for an empty dataset.")

    total_sum = sum(data)
    count = len(data)
    return total_sum / count