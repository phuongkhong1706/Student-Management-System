import time
import math
import threading


# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# Hàm tuần tự tìm số nguyên tố từ 1 đến N
def find_primes_sequential(N):
    primes = []
    for i in range(1, N + 1):
        if is_prime(i):
            primes.append(i)
    return primes


# Hàm đa luồng tìm số nguyên tố
def find_primes_parallel(N, num_threads):
    primes = []
    lock = threading.Lock()

    # Hàm tìm số nguyên tố trong 1 phần của dải số
    def find_primes_in_range(start, end):
        local_primes = []
        for i in range(start, end):
            if is_prime(i):
                local_primes.append(i)
        with lock:
            primes.extend(local_primes)

    # Chia công việc cho các luồng
    threads = []
    step = N // num_threads
    for i in range(num_threads):
        start = i * step + 1
        end = (i + 1) * step + 1 if i < num_threads - 1 else N + 1
        thread = threading.Thread(target=find_primes_in_range, args=(start, end))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return primes


# Hàm so sánh thời gian chạy
def compare_prime_algorithms(N, num_threads=4):
    # Phương pháp tuần tự
    start_time = time.time()
    primes_seq = find_primes_sequential(N)
    sequential_time = time.time() - start_time
    print(f"Số nguyên tố tuần tự: {len(primes_seq)} số")
    print(f"Thời gian tuần tự: {sequential_time:.4f} giây\n")

    # Phương pháp đa luồng
    start_time = time.time()
    primes_parallel = find_primes_parallel(N, num_threads)
    parallel_time = time.time() - start_time
    print(f"Số nguyên tố đa luồng: {len(primes_parallel)} số")
    print(f"Thời gian đa luồng: {parallel_time:.4f} giây\n")


# Chạy chương trình
if __name__ == "__main__":
    N = int(input("Nhập N: "))
    num_threads = int(input("Nhập số luồng: "))
    compare_prime_algorithms(N, num_threads)
