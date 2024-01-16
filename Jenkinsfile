pipeline {
   agent { docker { image 'mcr.microsoft.com/playwright/python:v1.40.0-jammy' } }
   stages {
        stage('install playwright') {
              steps {
                sh '''
                    python3 -m venv env
                    source ./env/bin/activate
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
                sh 'playwright install --with-deps'
                sh 'pytest'
              }

//       stage('e2e-tests') {
//          steps {
//             sh 'npm ci'
//             sh 'npx playwright install --with-deps'
//             sh '''pip install playwright
//                 playwright install --with-deps'''
//               // Устанавливаем пакеты в /usr/local
// //              sh 'pip install --no-cache-dir --user -r requirements.txt --ignore-installed'
//
//              // Запускаем тесты
//              sh 'pytest'
//
//          }



      }
   }
}