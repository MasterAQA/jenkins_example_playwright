pipeline {
   agent { docker { image 'mcr.microsoft.com/playwright/python:v1.40.0-jammy' } }
   stages {
      stage('e2e-tests') {
         steps {
            script {
               // Установка пакетов в другую директорию
               sh 'pip install --install-option="--prefix=/install" -r requirements.txt'

               // Убедимся, что исполняемый файл pytest доступен в PATH
               sh 'export PATH=$PATH:/install/bin'

               // Запуск тестов
               sh 'pytest'
            }
         }
      }
   }
}