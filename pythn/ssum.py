pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('build') {
            steps {
                sh """
                      a=5
                      b=3
                      c=a+b
                      echo
                      """
            }
        }
    }
}
