provider "aws" {
  region = var.region
}

module "my_ec2" {
  source        = "./modules/ec2"
  name          = var.instance_name
  ami           = var.ami
  instance_type = var.instance_type
  key_name      = var.key_name
  volume_size   = var.volume_size
}