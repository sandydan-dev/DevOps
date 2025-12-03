#todo: Basic EC2 Instance create
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "firstInstance" {
  ami                    = "ami-0fa3fe0fa7920f68e"   # ami amazon linux
  instance_type          = "t2.small"       # instance type
  key_name               = "k8sKey"      # key-pair name
  vpc_security_group_ids = ["sg-09df4133c962d11d4"] # sg-09df4133c962d11d4 (mysg) | 08428b044e78337d6 (default)

  root_block_device {
    volume_size = 12    # size of the volume
  }

  tags = {
    Name : "instanceamazon"    # this is AWS console EC2 instance name
  }
}


# todo: 