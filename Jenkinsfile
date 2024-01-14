/* Requires the Docker Pipeline plugin */
pipeline {
  agent {
    docker {
      image 'mcr.microsoft.com/playwright:v1.17.2-focal'
    }
  }
  stages {
    stage('install playwright') {
      steps {
        sh '''
          python -m playwright install
          python -m playwright install-deps
        '''
      }
    }
    stage('test') {
      steps {
        sh '''
          python playwright tests --list
          python playwright test
        '''
      }
      post {
        success {
          archiveArtifacts(artifacts: 'homepage-*.png', followSymlinks: false)
          sh 'rm -rf *.png'
        }
      }
    }
  }
}