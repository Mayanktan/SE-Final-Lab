pipeline {
    agent any

    environment {
        IMAGE = "mayanktan/se-final-lab:latest"
        VENV = ".venv"
        PYTHON = "/usr/bin/python3"
        PATH = "/usr/local/bin:$PATH"
    }

    stages {

                stage('Checkout') {
                        steps {
                                checkout([$class: 'GitSCM',
                                    branches: [[name: '*/main']],
                                    userRemoteConfigs: [[
                                        url: 'https://github.com/Mayanktan/SE-Final-Lab',
                                        credentialsId: 'githubcreds'
                                    ]]
                                ])
                        }
                }

        stage('Create Virtual Environment') {
            steps {
                sh '$PYTHON -m venv $VENV'
                sh '$VENV/bin/pip install --upgrade pip'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '$VENV/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh '$VENV/bin/pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker_creds',
                                                  usernameVariable: 'USER',
                                                  passwordVariable: 'PASS')]) {
                    sh '''
                      echo $PASS | docker login -u $USER --password-stdin
                      docker push $IMAGE
                    '''
                }
            }
        }

        stage('Deploy Container') {
                        steps {
                                sh '''
                                    docker pull $IMAGE
                                    docker stop ci-cd-demo || true
                                    docker rm ci-cd-demo || true
                                    docker run -d -p 5001:5000 --name ci-cd-demo $IMAGE
                                '''
                        }
        }
    }
}
