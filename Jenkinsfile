/* Requires the Docker Pipeline plugin */
pipeline {
    agent {
        docker { image 'python:3.10.6' }
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
                    docker.image('python:3.10.6').inside {
                        withEnv(['APPLE_USERNAME=${APPLE_USERNAME}',
                        'APPLE_PASSWORD=${APPLE_USERNAME}']) {
                            sh 'sudo python -m playwright install --user'
                            sh 'sudo python -m playwright install-deps --user'
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
