pipeline {
    agent {
        docker { image 'mcr.microsoft.com/playwright/python:v1.40.0-jammy' }
    }

    environment {
        APPLE_USERNAME = 'JIsyri6824'
        APPLE_PASSWORD = '51246243'
    }

    stages {
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Install playwright dependencies') {
            steps {
                script {
                    docker.image('mcr.microsoft.com/playwright/python:v1.40.0-jammy').inside {
                        withEnv(['MY_ENV_VAR=${MY_ENV_VAR}']) {
                            sh 'python -m playwright install'
                            sh 'python -m playwright install-deps'
                        }
                    }
                }
            }
        }

        stage('Run e2e tests') {
            steps {
                sh 'pytest'
            }
        }
    }
}
