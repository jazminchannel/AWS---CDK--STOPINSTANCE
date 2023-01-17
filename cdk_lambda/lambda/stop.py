import boto3

regions = [] #list of all regions
client = boto3.client('ec2')
response = client.describe_regions()
for item in response["Regions"]:
    regions.append(item["RegionName"])


def handler(event, context): #check each region for servers in running state and turn them off
     
    for region in regions: 
        instancelist = []
        ec2 = boto3.client('ec2', region_name=region)
        instances = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

        for reservation in instances['Reservations']:
            for instance in reservation['Instances']:
                instancelist.append(instance['InstanceId'])
                ec2.stop_instances(InstanceIds=instancelist)
                for id in instancelist:
                    print('stopped your instances: ' + str(id))
       