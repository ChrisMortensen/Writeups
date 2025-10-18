import requests
import time
from concurrent.futures import ThreadPoolExecutor

CHARSET = '_}' + '4bcd3f6h1jklmn0pqr57uvwxyz'

# Rate Limiting
MAX_RETRIES = 3
WAIT_BEFORE_RETRY = 1
WAIT_BETWEEN_REQUESTS = 0.2
MAX_WORKERS = 2

def query_oracle(query_string):
    url = f"http://example.com/oracle?q={query_string}" # Change to target website
    
    for attempt in range(MAX_RETRIES):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(WAIT_BEFORE_RETRY)
    return None

def best_candidate(known):
    results = {}
    
    def test_char(char):
        time.sleep(WAIT_BETWEEN_REQUESTS)
        response = query_oracle(known + char)
        if response is None:
            return char, 1000  # Return high value if failed
        return char, response['compressed_len']
    
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [executor.submit(test_char, char) for char in CHARSET]
        for future in futures:
            char, length = future.result()
            results[char] = length
            print(f"{char}: {length}")
            if length == 90: break # Realised 90 means correct
    
    best = min(results.items(), key=lambda x: x[1])
    return best

if __name__ == "__main__":
    known = 'poctf{uwsp_'
    
    while known[-1] != '}':
        char, length = best_candidate(known)
        known += char
        print(f"Current: {known}")
    
    print(f"Flag: {known}")