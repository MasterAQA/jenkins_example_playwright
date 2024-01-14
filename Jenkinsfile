pipeline {
   agent { docker { image 'mcr.microsoft.com/playwright/python:v1.40.0-jammy' } }
   stages {
      stage('e2e-tests') {
         steps {
            script {
            sh 'cd /usr/local'
              // Устанавливаем пакеты в /usr/local
             sh 'pip install --no-cache-dir --user -r requirements.txt --ignore-installed'

            // Запускаем тесты
            sh 'pytest'
            }
         }
      }
   }
}