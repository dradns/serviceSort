pipeline {
  agent {kubernetes { image 'python:3.7.2' }}
  stages {
    stage('unit') {
        steps{
            withPythonEnv('python3') {
                sh 'python --version'
                sh 'ls'
                sh 'pwd'
            }
        }
    }
  }
}
