import sys
import time
import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def visit_site(url):
    driver = webdriver.Chrome(executable_path='/')  # Update path to your chromedriver path
    
    try:
        driver.get(url)
        print(f"Visited: {url}")
        time.sleep(5)  # Wait for 5 seconds (adjust as needed)
    except Exception as e:
        print(f"Error visiting {url}: {e}")
    finally:
        driver.quit()

# Function to run multi-threaded visits
def run_threads(url, num_threads):
    threads = []
    
    for _ in range(num_threads):
        thread = threading.Thread(target=visit_site, args=(url,))
        thread.start()
        threads.append(thread)
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <site_url> <num_threads>")
        sys.exit(1)
    
    site_url = sys.argv[1]
    num_threads = int(sys.argv[2])
    
    if num_threads <= 0:
        print("Number of threads should be greater than 0.")
        sys.exit(1)
    
    run_threads(site_url, num_threads)
