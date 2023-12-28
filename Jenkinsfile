/* Requires the Docker Pipeline plugin */
pipeline {
    agent {
        dockerfile true
    }
    stages {
        stage('run from docker') {
            steps {
                sh 'python --version'
            }
        }
    }
}