/* Requires the Docker Pipeline plugin */
pipeline {
    agent {
        dockerfile true
    }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}