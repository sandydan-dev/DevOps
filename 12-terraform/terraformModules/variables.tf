variable "region" {
  default = "us-east-1"
}

variable "ami_id" {
  default = "ami-0fa3fe0fa7920f68e"
}

variable "instance_type" {
  default = "t2.small"
}

variable "key_name" {
  default = "k8sKey"
}

variable "volume_size" {
  default = 15
}

variable "instance_name" {
  default = "MyInstance"
}

variable "cidr_allow_all" {
  type    = list(string)
  default = ["0.0.0.0/0"]
}
