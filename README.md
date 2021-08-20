
# ELK Stack Automation Design

![](images/design.png)

Ansible playbook to deploy elk stack

Roles:
* docker - Install docker and python3-docker packages and checks if docker daemon is up and running
* elasticsearch - Deploys elasticsearch container
* kibana - Deploys Kibana container
* logstash - Deploys Logstash container
* heartbeat - Deploys uptime metric container
* metricbeat - Deploys container that collects host system metrics
* filebeat - Deploys container that forwards log files

## Deployment

Test connection

`ansible all -m ping -i inventory/ansible_hosts`

Deploy elk stack

`ansible-playbook -i inventory inventory/ansible_hosts elk.yml`

Deploy Specific role

`ansible-playbook -i inventory inventory/ansible_hosts elk.yml --tags logstash`