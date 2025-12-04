#todo: Basic EC2 Instance create
# provider "aws" {
#   region = "us-east-1"
# }

# resource "aws_instance" "firstInstance" {
#   ami                    = "ami-0fa3fe0fa7920f68e"   # ami amazon linux
#   instance_type          = "t2.small"       # instance type
#   key_name               = "k8sKey"      # key-pair name k8sKey
#   vpc_security_group_ids = ["sg-09df4133c962d11d4"] # 

#   root_block_device {
#     volume_size = 12    # size of the volume
#   }

#   tags = {
#     Name : "firsInstance1"    # this is AWS console EC2 instance name
#   }
# }


# todo: Create full controlled EC2 instance 

// aws provider and specific region
provider "aws" {
  region = "us-east-1"
}

// create EC2 resource 
resource "aws_instance" "my_instance" {
  ami                    = "ami-0fa3fe0fa7920f68e"
  instance_type          = "t2.small"
  key_name               = "k8sKey"
  user_data              = file("./script.sh")
  vpc_security_group_ids = [aws_security_group.example_sg.id] # attach SG to EC2 instance to run web content

  // define storage/volume size
  root_block_device {
    volume_size = 15
  }

  // aws console name as tag name
  tags = {
    Name = "ControllerEC2_3"
  }

}

// create security group 
resource "aws_security_group" "example_sg" {
  name        = "example_security_sg"
  description = "Allow SSH and HTTP rules"

  // inbound rule to allow SSH(22) rule for all through ssh connection
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] // open for all ssh through
  }

  // inboud rule to allow for publically for all HTTP traffic
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] // open for all traffic
  }

  // keep outbout as it is open to all (response)
  egress {
    from_port   = 0             // zero means for all
    to_port     = 0             // zero means for all
    protocol    = "-1"          # all protocol
    cidr_blocks = ["0.0.0.0/0"] // open for all traffic
  }

}

// "output" modules used for create Public and Private IP
// create public IP 
output "instance_public_ip" {
  description = "public IP of ec2 instance"
  value       = aws_instance.my_instance.public_ip
}

// creae private IP
output "instance_private_id" {
  description = "private IP of ec2 instance"
  value       = aws_instance.my_instance.private_ip
}