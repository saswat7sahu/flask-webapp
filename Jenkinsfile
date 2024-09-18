pipeline {
    agent any

   stages {
        stage('Clone Repository') {
            steps {
                // Clonning the repository 
                git branch: 'main', url: 'https://github.com/saswat7sahu/flask-webapp.git'
            }
        }

        stage('Set up Python Environment') {
            steps {
                script {
                    // Install dependencies
                    sh 'python3 -m venv venv'       // virtual environment
                    sh 'pwd'
                    sh '. venv/bin/activate && pip install -r recuirments.txt'// Install dependencies from the requirements file
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                    // Run the unit tests using unittest
                    sh '. venv/bin/activate && python -m unittest discover -s tests' // Assuming tests are in the 'tests' folder
                }
            }
        }
    }
}
