terraform {
  required_providers {
    dnacenter = {
      source = "cisco-en-programmability/dnacenter"
      version = "0.1.0-beta.2"
    }
  }
}

provider "dnacenter" {

  username = "<username>"
  password = "<password>"
  base_url = "https://<DNAC_IP>"
  debug = "false"
  ssl_verify = "false"
}



resource "dnacenter_global_pool" "response" {
  provider = dnacenter
  parameters {
    settings {
      ippool {
        ip_address_space = "IPv4"
        ip_pool_cidr     = "14.0.0.0/16"  <======== replace the subnet with your choice 
        ip_pool_name     = "tform-1"
        type             = "Generic"
      }
    }
  }
}


resource "dnacenter_reserve_ip_subpool" "example" {
  count=1

  provider = dnacenter
  parameters {
    ipv4_global_pool = "14.0.0.0/16"
     type               = "Generic"
    ipv4_dhcp_servers  = ["9.1.0.21"]
    ipv4_dns_servers   = ["9.1.0.21"]
    ipv4_gate_way      = "14.0.${count.index}.1"  <====== replace
    ipv4_prefix        = "true"
    ipv4_prefix_length = "24"
    ipv4_subnet        = "14.0.${count.index}.0"
    name    = "tform-reserve-${count.index}r"
    site_id = "05f34ee5-8f2d-4063-8391-b2a3d1998897"
  
    }
  }


  data "dnacenter_site" "example" {
    provider = dnacenter

  }

  output "dnacenter_site_example" {
    value = data.dnacenter_site.example.items
  }

/*
output "dnacenter_global_pool_example" {
  value = dnacenter_global_pool.response
}
output "dnacenter_reserve_ip_subpool_example" {
  value = dnacenter_reserve_ip_subpool.example
}
*/
