output "public_ip" {
  value = aws_instance.my_instance.public_ip
}

output "private_ip" {
  value = aws_instance.my_instance.private_ip
}

output "sg_id" {
  value = aws_security_group.this_sg.id
}
