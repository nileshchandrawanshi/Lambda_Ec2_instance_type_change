# Lambda_Ec2_instance_type_change
Use Lambda function to change the EC2 Instance machine type 
1. Introduction:
Start with an introduction that provides an overview of the Lambda function's purpose and what it does. Mention that it's designed to change the EC2 instance type running on AWS.

2. Prerequisites:
List the prerequisites and requirements for using the Lambda function. This should include:

AWS account with Lambda and EC2 access.
IAM roles with appropriate permissions for Lambda and EC2.
Knowledge of the AWS SDK for Python (Boto3).
The instance ID you want to modify and the desired instance type.
3. Setup:
Provide step-by-step instructions on how to set up the Lambda function:

3.1. Create a Lambda Function:
Log in to the AWS Management Console.
Navigate to the Lambda service.
Click "Create function."
Choose "Author from scratch."
Configure the function:
Function name: (Choose a name)
Runtime: Python 3.x
Execution role: (Create or choose an existing role with necessary permissions)
Click "Create function."
3.2. Upload the Code:
In the Lambda function editor, upload the Python code for the Lambda function.
Ensure that you include the necessary Boto3 import statement.
Save the code.
3.3. Configure Trigger (Optional):
If you want to trigger the Lambda function automatically (e.g., using an S3 event or an API Gateway), configure the trigger as needed.

