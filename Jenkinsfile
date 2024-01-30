pipeline {
    agent {
        docker {
            image 'mcr.microsoft.com/playwright/python:v1.32.1-jammy'
        }
    }


    stages{
        stage('Install requirements') {
              steps {
                  withEnv(["HOME=${env.WORKSPACE}"]) {
                          sh 'pip install --user -r requirements.txt'
                  }
              }
       }

       stage('Run tests') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                        sh 'SELENIUM_REMOTE_URL=http://192.168.100.4:4444 python -m pytest tests'
                    }
            }
       }

    }

        post {
                always {
                    // Архивируем артефакты сборки
                    archiveArtifacts artifacts: 'reports/report.xml'
                    archiveArtifacts artifacts: 'reports/html_report/**'
                    archiveArtifacts artifacts: 'reports/trace.zip'
                }
            }
}




