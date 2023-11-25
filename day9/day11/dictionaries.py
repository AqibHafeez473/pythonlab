ec2_instance_info = [
    {
        "Name": "ec2_1",
        "id": "4567",
        "type": "t2.micro"
    },
    {
         "Name": "ec2_2",
        "id": "9876",
        "type": "t2.micro"
    },
    {
         "Name": "ec2_3",
        "id": "190423",
        "type": "t2.micro"
    }
]

print(ec2_instance_info[2]["type"],ec2_instance_info[1]["id"])
