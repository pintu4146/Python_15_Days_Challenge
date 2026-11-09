import time


class Timer:
    def __enter__(self):
        print('entered in the timer')
        self.start_time = time.perf_counter()
        print("done with the enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.perf_counter()
        self.elapsed = self.end_time - self.start_time
        return  # returns none


with Timer() as pintu:
    t = [i for i in range(1000)]

print(f'{pintu.elapsed: .5f} ')
