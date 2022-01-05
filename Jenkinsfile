pipeline {
  agent {
        kubernetes {
            defaultContainer 'jnlp'
            yamlFile 'agentpod.yaml'
        }
    }
  stages {
    stage('unit') {
        steps{
            container('python3'){
                sh 'sleep 100'
                sh 'python --version'
                sh 'ls'
                sh 'pwd'
            }
        }
    }
  }
}
