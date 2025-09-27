pipeline {
    agent any

    stages {
        stage('Clone Git') {
            steps {
                git branch: 'main', url: 'https://github.com/bijeet1221/ScientificCalculator-SPE.git'
            }
        }

        stage('Build Calculator') {
            steps {
                echo "Running CLI Calculator..."
                sh "chmod +x calculator.py"
                sh "python3 calculator.py || true"  // || true to allow manual input
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running PyUnit Tests..."
                sh "python3 -m unittest test_calculator.py"
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker Image..."
                sh "docker build -t scientific-calculator:latest ."
            }
        }
    }
}

