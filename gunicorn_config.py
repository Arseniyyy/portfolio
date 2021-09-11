from multiprocessing import cpu_count


def max_workers():    
    return cpu_count()


max_requests = 1000
workers = max_workers()
timeout=120
