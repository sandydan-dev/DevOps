provider "aws" {
  region = var.region
}

// create ec2 instance 
resource "aws_instance" "my_name" {
  ami                    = var.my_ami
  instance_type          = var.instance_type
  key_name               = var.key_pair
  user_data              = file("./script.sh")
#   user_data_replace_on_change = true
  vpc_security_group_ids = [aws_security_group.my_sg.id] # attach sg to ec2 "aws_security_group.my_sg"

  // volume/storage 
  root_block_device {
    volume_size = var.volume_storage
  }

  tags = {
    Name = var.tag_name
  }
}

// create security group
resource "aws_security_group" "my_sg" {
  name        = "my_security_SG"
  description = "attach this SG to ece2 instance"

  // inboud rule for ssh access
  ingress {
    from_port   = var.ssh_port_range
    to_port     = var.ssh_port_range
    protocol    = var.protocol_tcp
    cidr_blocks = var.cidr_block_ip_range
  }

  // inboud rule for http allow traffic
  ingress {
    from_port   = var.http_port_range
    to_port     = var.http_port_range
    protocol    = var.protocol_tcp
    cidr_blocks = var.cidr_block_ip_range
  }


  // outbound rule to allow all traffic
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = var.protocol_m_1
    cidr_blocks = var.cidr_block_ip_range
  }
}


// ouput for associate default public IP
output "instance_public_ip" {
  description = "default public ip"
  value       = aws_instance.my_name.public_ip
}

// output for accociate default private ip
output "instance_private_ip" {
  description = "default private ip"
  value       = aws_instance.my_name.private_ip
}