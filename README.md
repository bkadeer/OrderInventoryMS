# Microservices Contract Testing with Pact

This project demonstrates contract testing between two microservices: the **Order Service** (consumer) and the **Inventory Service** (provider) using **Pact** and **pytest** in Python.

## Project Structure
.
├── order_service/
│   ├── init.py
│   ├── main.py
│   └── …
├── inventory_service/
│   ├── init.py
│   ├── main.py
│   └── …
├── tests/
│   ├── test_contract_inventory.py
│   └── …
├── pacts/
│   └── …
└── README.md

## Prerequisites

Make sure you have the following installed:

- Python 3.6 or higher
- Pip (Python package installer)
- Docker (for running services in containers)

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/microservices-contract-testing.git
cd microservices-contract-testing
```

2. Create a Virtual Environment
```bash

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```
## Running the Services

You can run the Order and Inventory Services using Docker. Here’s an example of how to do that:

# Build and run services
docker-compose up --build

Running Contract Tests

To run the contract tests, execute:
pytest tests/test_contract_inventory.py

Pact File

The Pact file will be generated after running the tests and will be located in the pacts/ directory. This file describes the interactions between the Order Service and Inventory Service.

Publishing the Pact

To publish the generated Pact file to a Pact Broker, use:
pact-broker publish pacts/ --broker-base-url http://your-broker-url --consumer-version 1.0.0

Make sure to replace http://your-broker-url with the actual URL of your Pact Broker.

Provider Verification

The Inventory Service should verify the Pact by fetching it from the Pact Broker. Implement provider verification in the Inventory Service:
from pact import Verifier

verifier = Verifier(provider='InventoryService', pact_broker_url='http://your-broker-url')
verifier.verify()
