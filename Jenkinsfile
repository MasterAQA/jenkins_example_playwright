pipeline {
   agent { docker { image 'mcr.microsoft.com/playwright/python:v1.40.0-jammy' } }
   stages {
      stage('e2e-tests') {
         steps {
//             sh 'sudo -H pip3 install --upgrade pip'
            sh '''python3 -m venv env
                 source ./env/bin/activate
                 python -m pip install package -r requirements.txt'''
            sh 'pytest'
         }
      }
   }
}