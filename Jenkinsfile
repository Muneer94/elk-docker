#!/usr/bin/env groovy

import jenkins.model.*;
import groovy.json.*

pipeline {
    agent any
    environment {
        CRED_ID = "0e2e4a1b-17ef-4112-9694-0c87163c4fd"
        INVENTORY_PATH = "inventory/ansible_hosts"
    }
    options {
        ansiColor('xterm')
    }
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
                ansiblePlaybook colorized: true, installation: 'Ansible', credentialsId: '${env.CRED_ID}', inventory: '${env.INVENTORY_PATH}', playbook: 'elk.yml',tags: "elasticsearch"
            }
        }
        stage('Deploy Kibana') {
            steps {
                ansiblePlaybook colorized: true, installation: 'Ansible', credentialsId: '${env.CRED_ID}', inventory: '${env.INVENTORY_PATH}', playbook: 'elk.yml',tags: "kibana"
            }
        }
        stage('Deploy Filebeat') {
            steps {
                ansiblePlaybook colorized: true, installation: 'Ansible', credentialsId: '${env.CRED_ID}', inventory: '${env.INVENTORY_PATH}', playbook: 'elk.yml',tags: "filebeat"
            }
        }
    }
}
