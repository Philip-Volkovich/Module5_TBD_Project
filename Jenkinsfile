pipeline {
    agent any

    environment {
        GIT_COMMITTER_NAME = 'Philip Volkovich'
        GIT_COMMITTER_EMAIL = 'lplb6400@gmail.com'
    }

    stages {
        stage('Set Git Configuration') {
            steps {
                // Set Git configuration
                sh "git config user.name '${GIT_COMMITTER_NAME}'"
                sh "git config user.email '${GIT_COMMITTER_EMAIL}'"
            }
        }

        stage('Checkout Feature Branch') {
            steps {
                // Checkout the feature1 branch
                git branch: 'feature1', url: 'https://github.com/Philip-Volkovich/DQI_Module5_PV.git'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                // Create a virtual environment
                sh 'python3 -m venv venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install dependencies from requirements.txt within the virtual environment
                sh './venv/bin/python3 -m pip install -r requirements.txt'
            }
        }

        stage('Testing') {
            steps {
                // Run tests on the feature branch
                sh './venv/bin/python3 main.py'
            }
        }

        stage('Rebase Feature Branch onto Main') {
            steps {
                // Rebase feature branch onto main
                sh 'git checkout feature1'
                sh 'git rebase main'
            }
        }

        stage('Update Main Branch') {
            steps {
                // Update main branch with the rebased feature branch
                sh 'git checkout main'
                sh 'git merge feature1'
            }
        }

        stage('Delete Feature Branch') {
            steps {
                // Delete the feature1 branch
                sh "git push origin --delete feature1"
            }
        }
    }
}
