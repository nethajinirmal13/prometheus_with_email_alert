from prometheus_client import start_http_server, Counter, Gauge
import random
import time

# Define a counter metric to count the number of requests
REQUESTS = Counter('app_requests_total', 'Total number of requests')

# Define a gauge metric to simulate the temperature of a server
TEMPERATURE = Gauge('server_temperature_celsius', 'Current server temperature in Celsius')

def process_request():
    """A dummy function to simulate processing a request."""
    REQUESTS.inc()  # Increment the requests counter
    temp = random.uniform(88.0, 100.0)
    TEMPERATURE.set(temp)  # Set the temperature gauge
    print(f"Processed request: Temperature is {temp:.2f}°C")
    time.sleep(1)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    #start_http_server(8000)
    start_http_server(8000, addr="0.0.0.0")

    print("Serving metrics on http://localhost:8000/metrics")

    # Simulate requests being processed
    while True:
        process_request()
