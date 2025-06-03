# Load Balancer
- used to manage cluster of services
- frontend ports AKA Listeners => 80, 443
- backend ports services running => 80 443
- can have a cluster in multiples zones and a single endpoint using a load balancer
## Types of load balancers in AWS
- Application
- Network 
- Classic

### Classic
- accept traffice and serve it ot the backend
### Application
- 7 layer load balancer => fits in the OSI Model
##### IMP 
- only used for http && https requests
###### ex
- like amazon.com/reg or /login
### Network
- OSI layer 4
- can handle millions of requests
- static IP
## how to setup
- first launch the site on the ec2 instance
- create AMI from it => similar to snapshot with metadata
- lauch template
- then load balancer

