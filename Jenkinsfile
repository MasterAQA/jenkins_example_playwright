pipeline {
    agent {
        docker {
            image 'python:3.10.6'
        }
    }

    stages {
        stage('Install dependencies') {
            steps {
                script {
                    sh 'apt-get -yqq update && apt-get -yqq upgrade'
                    sh 'apt-get install -yqq python3 python3-pip software-properties-common wget unzip'
                }
            }
        }

        stage('Setup environment') {
            steps {
                script {
                    // Copy files to the workspace
                    sh 'cp -r ./* $WORKSPACE/'
                    dir('$WORKSPACE') {
                        // Install Python dependencies
                        sh 'pip3 install -r requirements.txt'

                        // Install Playwright and its dependencies
                        sh 'python3 -m playwright install'
                        sh 'python3 -m playwright install-deps'
                    }
                }
            }
        }

        stage('Run tests') {
            steps {
                script {
                    // Run pytest
                    sh 'python3 -m pytest'
                }
            }
        }
    }
}
