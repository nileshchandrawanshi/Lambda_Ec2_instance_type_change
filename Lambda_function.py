import boto3

def lambda_handler(event, context):
    # Initialize EC2 client
    ec2 = boto3.client('ec2')
    
    # Specify the instance ID and the new instance type
    instance_id = 'i-01e1b11d59b195744'  #----------------- Specify your instance ID Here
    new_instance_type = 't3.nano'  #<<--------------------- Change this to the desired instance type
    
    try:
        # Stop the instance
        ec2.stop_instances(InstanceIds=[instance_id])
        waiter = ec2.get_waiter('instance_stopped')
        waiter.wait(InstanceIds=[instance_id])
        
        # Modify the instance type
        ec2.modify_instance_attribute(
            InstanceId=instance_id,
            InstanceType={
                'Value': new_instance_type
            }
        )
        
        # Start the instance
        ec2.start_instances(InstanceIds=[instance_id])
        waiter = ec2.get_waiter('instance_running')
        waiter.wait(InstanceIds=[instance_id])
        
        return {
            'statusCode': 200,
            'body': f'Changed instance type of {instance_id} to {new_instance_type}'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
