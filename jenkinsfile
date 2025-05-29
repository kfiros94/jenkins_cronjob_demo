pipeline {
  agent any
  triggers {
    cron('*/1 * * * *')
  }
  stages {
    stage('Run Python script') {
      steps {
        bat 'python my_script.py'
      }
    }
  }
}
