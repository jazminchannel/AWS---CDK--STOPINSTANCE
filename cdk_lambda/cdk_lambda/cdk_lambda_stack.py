from constructs import Construct
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
      aws_events as events,
    aws_events_targets as targets,
)


class CdkLambdaStack(Stack):
    
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Defines an AWS Lambda Resource

        my_lambda = _lambda.Function(
            self, 'StopHandler', 
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset('lambda'),
            handler='stop.handler',
        )

         # Adding Event Bridge Rule
        rule = events.Rule(self, "Rule",
        schedule=events.Schedule.cron(minute="30", hour="20")
    )
        rule.add_target(targets.LambdaFunction(my_lambda))
