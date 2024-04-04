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

        stage('Rebase Feature Branch onto Main') {
            steps {
                // Checkout main branch and pull latest changes
                sh 'git checkout main'
                sh 'git pull'

                // Checkout feature1 branch and rebase onto main
                sh 'git checkout feature1'
                sh 'git rebase main'
            }
        }

        stage('Testing') {
            steps {
                // Run tests on the feature branch
                sh './venv/bin/python3 main.py'
            }
        }

        stage('Commit Changes on Feature Branch') {
            steps {
                // Add all changes to the staging area
                sh 'git add .'
                // Commit changes on the feature branch
                sh 'git commit -m "Commit changes on feature1 branch"'
            }
        }

        stage('Merge into Main') {
            steps {
                // Merge feature branch into main
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
