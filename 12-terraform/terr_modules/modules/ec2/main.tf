
# this is Security Group 
resource "aws_security_group" "this_sg" {
  name = "my_security_group"
  description = "Security group for EC2 module"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

// AWS resource instance

resource "aws_instance" "my_instance" {
  ami = "var.ami"
  instance_type = "var.instance_type"
  key_name = "var.key_name"
  vpc_security_group_ids = [aws_security_group.this_sg.id]
  
  user_data = file("./script.sh")

  root_block_device {
    volume_size = var.volume_size
  }

  tags = {
    Name = var.name
  }
}