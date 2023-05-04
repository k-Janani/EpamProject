pipeline {
    agent any
    
    stages {
        stage('Welcome') {
            steps {
                echo 'Welcome to SeedToFeed website!'
            }
        }
    }
}
