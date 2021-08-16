#!/usr/bin/env groovy

import jenkins.model.*;
import groovy.json.*

pipeline {
    agent any
    environment {
        CRED_ID = '0e2e4a1b-17ef-4112-9694-0c87163c4fd8'
        INVENTORY_PATH = 'inventory/ansible_hosts'
    }
    options {
        ansiColor('xterm')
    }
    stages {
        stage('Lint Code') {
            steps {
                script {
                    sh 'ansible-lint elk.yml'
                }
            }
        }
        stage('Sample') {
            when {
                anyOf {
                    changeset "vars/**"
                    changeset "inventory/**"
                }
            }
            steps {
                script {
                    echo "Muneer"
                }
            }
        }
        stage('Deploy ElasticSearch') {
            when {
                anyOf {
                    changeset "vars/**"
                    changeset "inventory/**"
                    changeset "roles/elasticsearch/**"
                }
            }
            steps {
                ansiblePlaybook colorized: true, installation: "Ansible", credentialsId: "${env.CRED_ID}", inventory: "${env.INVENTORY_PATH}", playbook: "elk.yml",tags: "elasticsearch"
            }
        }
        stage('Deploy Kibana') {
            when {
                anyOf {
                    changeset "vars/**"
                    changeset "inventory/**"
                    changeset "roles/kibana/**"
                }
            }
            steps {
                ansiblePlaybook colorized: true, installation: "Ansible", credentialsId: "${env.CRED_ID}", inventory: "${env.INVENTORY_PATH}", playbook: "elk.yml",tags: "kibana"
            }
        }
        stage('Deploy Logstash') {
            when {
                anyOf {
                    changeset "vars/**"
                    changeset "inventory/**"
                    changeset "roles/logstash/**"
                }
            }
            steps {
                ansiblePlaybook colorized: true, installation: "Ansible", credentialsId: "${env.CRED_ID}", inventory: "${env.INVENTORY_PATH}", playbook: "elk.yml",tags: "logstash"
            }
        }
        stage('Deploy Filebeat') {
            when {
                anyOf {
                    changeset "vars/**"
                    changeset "inventory/**"
                    changeset "roles/filebeat/**"
                }
            }
            steps {
                ansiblePlaybook colorized: true, installation: "Ansible", credentialsId: "${env.CRED_ID}", inventory: "${env.INVENTORY_PATH}", playbook: "elk.yml",tags: "filebeat"
            }
        }
        stage('Deploy Hearbeat') {
            when {
                anyOf {
                    changeset "vars/**"
                    changeset "inventory/**"
                    changeset "roles/heartbeat/**"
                }
            }
            steps {
                ansiblePlaybook colorized: true, installation: "Ansible", credentialsId: "${env.CRED_ID}", inventory: "${env.INVENTORY_PATH}", playbook: "elk.yml",tags: "heartbeat"
            }
        }
    }
}
