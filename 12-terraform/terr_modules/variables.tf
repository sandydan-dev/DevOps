variable "region" {
  default = "us-east-1"
}

variable "ami" {
  default = "ami-0fa3fe0fa7920f68e"
}

variable "instance_name" {
  default = "Module-Instance"
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
