// variable for region
variable "region" {
  description = "aws instance region"  
  type = string
  default = "us-east-1"
}

// var for aws ami
variable "my_ami" {
  default = "ami-0fa3fe0fa7920f68e"
  type = string
  description = "AMI id"
}

// var for instance type RAM, CPU uses
variable "instance_type" {
  default = "t2.small"
  type = string
  description = "Instance type Ram, CPU uses"
}

// var for key-pair name
variable "key_pair" {
  default = "k8sKey"
  type = string 
  description = "Already created key pair name for ssh"
}

// var for volume blocks
variable "volume_storage" {
  default = 15
  type = number
  description = "define ec2 instance storage"
}


// var for tag name
variable "tag_name" {
  default = "Instance_2"
  type = string
  description = "AWS console ec2 instance name"
}


// variable for security group
// ingress for ssh 22 port
variable "ssh_port_range" {
  default = 22
  type = number
  description = "ssh 22 port range"
}

// ingress for http port range 
variable "http_port_range" {
  default = 80
  type = number
  description = "http 80 port range for web content"
}

// variable for protocol ingress 'tcp' (inbount)
variable "protocol_tcp" {
  default = "tcp"
  type = string
  description = "tcp protocol for request and response"
}

// varible for protocol egress '-1' outbound for all responses
variable "protocol_m_1" {
  default = "-1"
  type = string
  description = "egress protocol for all"
}

// variable for cidr block
variable "cidr_block_ip_range" {
  default = ["0.0.0.0/0"]
  type = list(string)
  description = "cidr block ip range"
}
