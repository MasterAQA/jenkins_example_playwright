pipeline {
   agent { docker { image 'mcr.microsoft.com/playwright/python:v1.40.0-jammy' } }
   stages {
      stage('e2e-tests') {
         steps {
            script {
            sh '''wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py --user
                  cd .local/bin
                  ./pip install -r requirements.txt --user'''
              // Устанавливаем пакеты в /usr/local
//              sh 'pip install --no-cache-dir --user -r requirements.txt --ignore-installed'

             // Запускаем тесты
             sh 'pytest'
            }
         }
      }
   }
}