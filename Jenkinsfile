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
        // stage('Quality Check') {
        //     def scannerHome = tool 'sonar';
        //     withSonarQubeEnv() {
        //         sh "${scannerHome}/bin/sonar-scanner"
        //     }
        // }

        stage('SonarQube analysis') {
            steps {
                script {
                    def scannerHome = tool 'sonar';
                    withSonarQubeEnv("sonar") {
                        sh "${scannerHome}/bin/sonar-scanner --version"
                        sh "java version"
                        // sh "${scannerHome}/bin/sonar-scanner  -Dsonar.projectKey=elk-docker -Dsonar.sources=.  -Dsonar.host.url=http://10.60.61.10:9000 -Dsonar.login=d041342358a913d9cd211805311ddd22ceff3abf"
                    }
                }
            }
        }
        stage("Quality gate") {
            steps {
                waitForQualityGate abortPipeline: true
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