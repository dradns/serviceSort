pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('unit') {
        withPythonEnv('python3') {
            sh 'python --version'
            sh 'ls'
            sh 'pwd'
        }}}}
