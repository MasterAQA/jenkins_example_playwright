/* Requires the Docker Pipeline plugin */
pipeline {
    agent {
        docker { image 'python:3.10.6' }
    }
    stages {
        stage('run from docker') {
            steps {
                sh 'python --version'
            }
        }
    }
}