variable "AWS_REGION" {
  default = "eu-west-1"
}
variable "PATH_TO_PRIVATE_KEY" {
  default = "mykey2"
}
variable "PATH_TO_PUBLIC_KEY" {
  default = "mykey2.pub"
}
variable "AMIS" {
  type = "map"
  default = {
    eu-west-1 = "ami-8fd760f6"
  }
}
variable "INSTANCE_DEVICE_NAME" {
  default = "/dev/xvdh"
}
