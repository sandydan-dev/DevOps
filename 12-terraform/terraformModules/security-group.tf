

resource "aws_security_group" "my_sg" {
  name = "my_security_group"
  description = "Security group for EC2"

# inboud rule for ssh connection to login 
    ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = var.cidr_allow_all   // ["0.0.0.0/0"]
  }

  // inbound rule for http 80 port web content
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = var.cidr_allow_all
  }

  // outbound rule for all traffic
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = var.cidr_allow_all
  }

}
