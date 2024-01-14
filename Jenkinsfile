pipeline {
   agent { docker { image 'mcr.microsoft.com/playwright/python:v1.40.0-jammy' } }
   stages {
      stage('e2e-tests') {
         steps {
            script {
              // Устанавливаем пакеты в /usr/local
             sh 'pip install --user --prefix=/usr/local -r requirements.txt'

             // Запускаем тесты
             sh 'pytest'
            }
         }
      }
   }
}