# test_contract_inventory.py

import requests
from pact import Consumer, Provider

def run_contract_test():
    # Define the Pact between Order Service (consumer) and Inventory Service (provider)
    pact = Consumer("OrderService").has_pact_with(Provider("InventoryService"), port=8001)
    pact.start_service()  # Start the mock service

    # Define the expected response from the Inventory Service
    expected = {
        "id": "A001",
        "name": "Laptop",
        "availability_status": "InStock"
    }

    # Set up Pact mock interaction
    (pact
     .given("Product A001 exists and is in stock")  # Precondition setup
     .upon_receiving("a request for product availability with id A001")  # Description of the request
     .with_request("GET", "/inventory/A001")  # Request details
     .will_respond_with(200, body=expected))  # Expected response

    with pact:  # This context ensures the mock server is running for the duration of this block
        # This simulates the request that the Order Service would make
        result = requests.get("http://localhost:8001/inventory/A001")
        
        # Assertions to validate the response
        assert result.status_code == 200, f"Expected status code 200 but got {result.status_code}"
        assert result.json() == expected, f"Expected response {expected} but got {result.json()}"

    pact.stop_service()  # Stop the mock service after tests are done

if __name__ == "__main__":
    try:
        run_contract_test()
        print("Contract test passed successfully.")
    except AssertionError as e:
        print(f"Contract test failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")