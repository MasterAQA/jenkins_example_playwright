pipeline {
   agent { docker { image 'mcr.microsoft.com/playwright/python:v1.40.0-jammy' } }
   stages {
        stage('install playwright') {
              steps {
                sh '''
                  python -m pip install --upgrade pip --user
                  pip install -r requirements.txt --user
                '''
                sh 'playwright install --with-deps --user'
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