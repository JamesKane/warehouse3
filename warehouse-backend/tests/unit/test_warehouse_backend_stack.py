import aws_cdk as core
import aws_cdk.assertions as assertions

from warehouse_backend.warehouse_backend_stack import WarehouseBackendStack

# example tests. To run these tests, uncomment this file along with the example
# resource in warehouse_backend/warehouse_backend_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = WarehouseBackendStack(app, "warehouse-backend")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
