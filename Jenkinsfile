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
        //     tools {
        //         jdk "jdk11" // the name you have given the JDK installation in Global Tool Configuration
        //     }
        //     steps {
        //         script {
        //             def scannerHome = tool "sonar";
        //             withSonarQubeEnv(credentialsId: "sonarqube") {
        //                 sh "${scannerHome}/bin/sonar-scanner"
        //             }
        //         }
        //     }
        // }
        // stage("Quality gate") {
        //     steps {
        //         waitForQualityGate webhookSecretId: 'sonarqube', abortPipeline: true
        //     }
        // }
        stage('Testing') {
            tools {
                dockerTool "docker"
            }
            // agent {
            //     docker { image 'selenium/standalone-chrome' }
            // }
            steps {
                script {
                    def dockerHome = tool "docker";
                    sh "echo ${dockerHome}"
                    ${dockerHome}.image("selenium/standalone-chrome").inside {
                        sh "python3 --version"
                    }
                }
            }
        }
        //     steps {
        //         sh 'python3 --version'
        //     }
        // }
        stage('ElasticSearch') {
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
        stage('Kibana') {
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
        stage('Logstash') {
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
        stage('Filebeat') {
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
        stage('Hearbeat') {
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