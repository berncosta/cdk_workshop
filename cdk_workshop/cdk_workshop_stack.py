from constructs import Construct
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)

from .hitcounter import HitCounter


class CdkWorkshopStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # defines lambda resource
        my_lambda = _lambda.Function(
            self,
            'Hello Handler',
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset('lambda'),
            handler='hello.handler',
        )

        # defines the hitcounter Lambda
        hello_with_hitcounter = HitCounter(
            self,
            id='HelloHitCounter',
            downstream=my_lambda,
        )

        # defines an API Gateway connected to our Lambda
        apigw.LambdaRestApi(
            self,
            id='Endpoint',
            handler=hello_with_hitcounter.handler,
        )

