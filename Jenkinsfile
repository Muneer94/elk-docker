import jenkins.model.*;
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
        stage('Ansible Test') {
            steps {
                script {
                    sh 'ls -la'
                    sh 'which ansible'
                }
                // ansiblePlaybook credentialsId: '0e2e4a1b-17ef-4112-9694-0c87163c4fd8', inventory: 'inventory/ansible_hosts', playbook: 'elk.yml'

                // ansiblePlaybook colorized: true, installation: 'Ansible', credentialsId: '0e2e4a1b-17ef-4112-9694-0c87163c4fd8', inventory: 'inventory/ansible_hosts', playbook: 'elk.yml',tags: "jenkins"
            }
        }
    }
}
