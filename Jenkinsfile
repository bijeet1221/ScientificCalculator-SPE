pipeline {
    agent any

    environment {
        IMAGE_NAME = 'bijeet1221/scientific-calculator'
        VENV_PATH = '/home/bijeet/Desktop/course/sem 7/SPE/workspace/ScientificCalculator/ansible-venv'
    }

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
                sh "docker build -t ${IMAGE_NAME}:latest ."
            }
        }

        stage('Push Docker Image to Registry') {
            steps {
                echo 'Pushing Docker image to DockerHub...'
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'docker-credentials') {
                        docker.image("${IMAGE_NAME}:latest").push()
                    }
                }
            }
        }

       stage('Deploying Our Application') {
            steps {
                echo 'Deploying via Ansible...'
                sh """
                    export LC_ALL=C.UTF-8
                    export LANG=C.UTF-8
                    \"${VENV_PATH}/bin/ansible-playbook\" -i inventory.ini playbook.yml
                """
            }
        }

        post {
            always {
                // Send plain text email notification with build status
                script {
                    def jobName = env.JOB_NAME
                    def buildNumber = env.BUILD_NUMBER
                    def pipelineStatus = currentBuild.result ?: 'UNKNOWN'
                    def buildUrl = env.BUILD_URL

                    def body = """
                    Jenkins Build Notification

                    Job Name: ${jobName}
                    Build Number: ${buildNumber}
                    Status: ${pipelineStatus.toUpperCase()}

                    You can check the console output at:
                    ${buildUrl}console
                    """

                    emailext(
                        subject: "${jobName} - Build #${buildNumber} - ${pipelineStatus.toUpperCase()}",
                        body: body,
                        to: "bijeet.basak2018@gmail.com",
                        from: "bijeet.basak2018@gmail.com",
                        replyTo: "bijeet.basak2018@gmail.com",
                        mimeType: 'text/plain'
                    )
                }
            }
        }
    }
}
