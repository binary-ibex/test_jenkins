pipeline {
    agent any
    stages {
        stage("verify tooling") {
            steps {
                sh '''
                docker info 
                docker version
                docker compose version
                curl --version
                jenkins --version
                '''
            }
        }
        stage("Starting container") {
            steps {
                sh '''
                docker compose up --no-color --wait -d
                docker compose ps
                '''
            }
        } 
        stage("Run test agains the container") {
            steps {
                sh 'curl localhost:8112'
            }
        }
        
    }
    post {
            always {
                sh 'docker compose down --remove-orphans -v'
            }
        }
}