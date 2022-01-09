pipeline {
  agent {
        kubernetes {
            defaultContainer 'containerAgentName'
            yamlFile 'agentpod.yaml'
        }
    }
  stages {
    stage('build') {
        steps{
            container('python3'){
                withPythonEnv('python3'){
                    sh 'pip install -r requirements.txt'
                    sh 'python --version'
                }
            }
        }
    }
    stage('unit') {
        steps{
            container('python3'){
                withPythonEnv('python3'){
                    sh 'pwd'
                    sh 'cd app'
                    sh 'pytest --junitxml results.xml || true'
                    junit "results.xml"
                }
            }
        }
    }
  }
}
