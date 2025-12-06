variable "name" {
  type        = string
  description = "Instance Name"
}

variable "ami" {
  type        = string
}

variable "instance_type" {
  type        = string
}

variable "key_name" {
  type        = string
}

variable "volume_size" {
  type        = number
  default     = 15
}
