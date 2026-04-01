import time

def retry(func, retries=3):
    for i in range(retries):
        try:
            return func()
        except Exception as e:
            print(f"Retry {i+1}:", e)
            time.sleep(2 * (i + 1))
    return "Failed after retries"