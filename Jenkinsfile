pipeline {
   agent { docker { image 'mcr.microsoft.com/playwright/python:v1.40.0-jammy' } }
   stages {
      stage('e2e-tests') {
         steps {
            script {
               // Устанавливаем пакеты в другую директорию
              sh 'PYTHONUSERBASE=/install pip install --user -r requirements.txt'

              // Убеждаемся, что исполняемый файл pytest доступен в PATH
              sh 'export PATH=$PATH:/install/bin'

              // Запускаем тесты
              sh 'pytest'
            }
         }
      }
   }
}