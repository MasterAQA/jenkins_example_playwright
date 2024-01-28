pipeline {
//     stages{
//         stage('Install Playwright') {
//             steps{
//                 agent {
//                     docker {
//                         image 'mcr.microsoft.com/playwright/python:v1.32.1-jammy'
//                     }
//                 }
//             }
//         }
    agent none
    stages {
        stage('Install Playwright') {
            agent { docker { image 'mcr.microsoft.com/playwright/python:v1.32.1-jammy'} }
//             steps {
//                 echo 'Hello, Maven'
//                 sh 'mvn --version'
//             }
        }


//         stage('Setup Selenium Grid') {
//             steps {
//                 // Установка и запуск Selenium Grid
//                 sh 'java -jar selenium-server-4.17.0.jar standalone --selenium-manager true --session-timeout 999999 --session-request-timeout 999999 --max-sessions 5'
//                 }
//             }
//     stages{
        stage('install requirements') {
              steps {
                  withEnv(["HOME=${env.WORKSPACE}"]) {
                          sh 'pip install --user -r requirements.txt'
//                           sh 'python -m pip install --upgrade pip'
//                           stash includes: 'users.txt', name: 'fileStash'
//                           sh 'sudo chmod 777 /var/lib/jenkins/workspace/'
//                           sh 'cp users.txt /var/lib/jenkins/workspace/'
//                                       sh 'playwright install --with-deps'
//                           sh 'SELENIUM_REMOTE_URL=http://192.168.100.4:4444 python -m pytest tests'
                  }
              }
       }
       stage('Run tests') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
//                                         sh 'python -m pip install --upgrade pip'
                        sh 'SELENIUM_REMOTE_URL=http://192.168.100.4:4444 python -m pytest tests'
                    }
//                 sh '''
//                     sudo apt install python3.10-venv
//                     python -m venv env
//                     source ./env/bin/activate
//                     python -m pip install --upgrade pip
//                     pip install -r requirements.txt
//                 '''
//                 sh 'playwright install --with-deps'
//                 sh 'pytest'
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