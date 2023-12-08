from fastapi.testclient import TestClient
from ..controllers import orders as controller
from ..main import app
import pytest
from ..models import order as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_order(db_session):
    # Create a sample order
    order_data = {
        "status": "pending",
        "customer_name": "Test",
        "customer_address": "Test Road",
        "customer_email": "test@email.com",
        "customer_phone": "123",
        "customer_comments": "comment",
        "payment_information": "123",
        "payment_status": "pending",
        "payment_type": "card"
    }

    order_object = model.Order(**order_data)

    # Call the create function
    created_order = controller.create(db_session, order_object)

    # Assertions
    assert created_order.status == order_data["status"]
    assert created_order.customer_name == order_data["customer_name"]
    assert created_order.customer_address == order_data["customer_address"]
    assert created_order.customer_email == order_data["customer_email"]
    assert created_order.customer_phone == order_data["customer_phone"]
    assert created_order.customer_comments == order_data["customer_comments"]
    
    assert created_order.payment_information == order_data["payment_information"]
    assert created_order.payment_status == order_data["payment_status"]
    assert created_order.payment_type == order_data["payment_type"]
    
