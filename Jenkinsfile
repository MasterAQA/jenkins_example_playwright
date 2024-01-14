pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'python:3.10.6'
        APPLE_USERNAME = 'JIsyri6824'
        APPLE_PASSWORD = '51246243'
    }

    stages {
        stage('Install dependencies') {
            steps {
                script {
                    docker.image(DOCKER_IMAGE).run("-v ${pwd()}/:/app") {
                        sh 'pip install -r /app/requirements.txt'
                    }
                }
            }
        }

        stage('Install playwright dependencies') {
            steps {
                script {
                    docker.image(DOCKER_IMAGE).inside("-v ${pwd()}/:/app") {
                        withEnv(['APPLE_USERNAME=${APPLE_USERNAME}',
                                'APPLE_PASSWORD=${APPLE_PASSWORD}']) {
                            sh 'python -m playwright install'
                            sh 'python -m playwright install-deps'
                        }
                    }
                }
            }
        }

        stage('Run e2e tests') {
            steps {
                script {
                    docker.image(DOCKER_IMAGE).run("-v ${pwd()}/:/app") {
                        sh 'pytest'
                    }
                }
            }
        }
    }
}