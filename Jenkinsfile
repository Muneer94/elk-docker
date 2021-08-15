import jenkins.model.*;
import hudson.plugins.ec2.*;
import groovy.json.*

pipeline {
    agent any
    stages {
        stage('Sample') {
            steps {
                script {
                    echo "Muneer"
                }
            }
        }
        stage('Deploy ElasticSearch') {
            steps {
                ansiblePlaybook colorizedOutput: true, installation: 'Ansible', credentialsId: '0e2e4a1b-17ef-4112-9694-0c87163c4fd8', inventory: 'inventory/ansible_hosts', playbook: 'elk.yml',tags: "elasticsearch"
            }
        }
        stage('Deploy Kibana') {
            steps {
                ansiblePlaybook colorizedOutput: true, installation: 'Ansible', credentialsId: '0e2e4a1b-17ef-4112-9694-0c87163c4fd8', inventory: 'inventory/ansible_hosts', playbook: 'elk.yml',tags: "kibana"
            }
        }
        stage('Deploy Filebeat') {
            steps {
                ansiblePlaybook colorizedOutput: true, installation: 'Ansible', credentialsId: '0e2e4a1b-17ef-4112-9694-0c87163c4fd8', inventory: 'inventory/ansible_hosts', playbook: 'elk.yml',tags: "filebeat"
            }
        }
    }
}
