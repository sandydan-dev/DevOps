# provider "aws" {
#   region = "us-east-1"
# }

# resource "aws_instance" "my_intance" {
#   ami                    = "ami-0fa3fe0fa7920f68e"
#   instance_type          = "t2.small"
#   key_name               = "k8sKey"
#   user_data              = file("./script.sh")
#   vpc_security_group_ids = [aws_security_group.my_sg] // this will connected with sg

#   root_block_device {
#     volume_size = 15
#   }

#   tags = {
#     Name = "MyInstance"
#   }
# }

# // resource security group ids

# resource "aws_security_group" "my_sg" {
#   name        = "my_security_group"
#   description = "attach sg to vpc_security_groups_ids"


#   // inboud rule for ssh 22 port login to ec2 instance
#   ingress {
#     from_port   = 22
#     to_port     = 22
#     protocol    = "tcp"
#     cidr_blocks = ["0.0.0.0/0"]
#   }

#   // inbound rule for http 80 port web content
#   ingress {
#     from_port   = 80
#     to_port     = 80
#     protocol    = "tcp"
#     cidr_blocks = ["0.0.0.0/0"]
#   }

#   // outbound rule for all traffic
#   egress {
#     from_port   = 0
#     to_port     = 0
#     protocol    = "-1"
#     cidr_blocks = ["0.0.0.0/0"]
#   }

# }


# // output for public ip
# output "instance_public_ip" {
#   value = aws_instance.my_intance.public_ip
#   description = "this is public ip"
# }

# // output for private ip
# output "instance_private_ip" {
#   value = aws_instance.my_intance.private_ip
#   description = "this is private ip"
# }


#todo:   new instance .tf files

resource "aws_instance" "my_intance" {
  ami = var.ami_id
  instance_type = var.instance_type
  key_name =  var.key_name 
  user_data = file("./script.sh")
  vpc_security_group_ids = [aws_security_group.my_sg.id]

  root_block_device {
    volume_size = var.volume_size
  }

  tags = {
    Name = var.instance_name 
  }
}