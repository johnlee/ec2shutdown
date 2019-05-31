import boto3
region = 'us-west-2'
ec2 = boto3.resource('ec2')

# Published through TFS
def lambda_handler(event, context):
    # Stop intances based on tag
    filters = [{
            'Name': 'tag-key',
            'Values': ['autoshutdown']
        },
        {
            'Name': 'instance-state-name', 
            'Values': ['running']
        }
    ]

    filteredInstances = ec2.instances.filter(Filters=filters)
    Instances = [instance.id for instance in filteredInstances]

    # Perform shutdown
    if len(Instances) > 0:
        result = ec2.instances.filter(InstanceIds=Instances).stop()
        print (result)
    else:
        print ("No instances to shutdown")