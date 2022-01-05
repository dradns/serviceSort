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
                sh 'python --version'
                sh 'ls'
                sh 'pwd'
            }
        }
    }
  }
}
