import pytest
from pact import Consumer, Provider
import requests

# Define the Pact between Order Service (consumer) and Inventory Service (provider)
pact = Consumer("OrderService").has_pact_with(Provider("InventoryService"), port=8002)

@pytest.fixture(scope="module", autouse=True)
def pact_setup_teardown():
    pact.start_service()  # Start the mock service
    yield
    pact.stop_service()  # Stop the mock service

def test_get_product_availability():
    expected_response = {
        "id": "A001",
        "name": "Laptop",
        "availability_status": "InStock"
    }

    # Set up Pact interaction
    pact.given("Product A001 exists and is in stock") \
        .upon_receiving("a request for product availability") \
        .with_request("GET", "/inventory/A001") \
        .will_respond_with(200, body=expected_response)

    with pact:
        # Simulate the request from the Order Service to the Pact mock service
        response = requests.get("http://localhost:8002/inventory/A001")
        
        # Assertions to verify the response
        assert response.status_code == 200
        assert response.json() == expected_response