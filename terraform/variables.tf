variable "prefix" {
  description = "The prefix used for all resources in this environment"
}

variable "loggly_token" {
  description = "Token for Loggly logging service"
  sensitive   = true
}