pipeline {
  agent any
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
