pipeline {
  agent any

  triggers {
    githubPush()
  }

  environment {
    GITHUB_REPO_URL = 'https://github.com/your-username/Playwright_Framework.git'
    GITHUB_BRANCH = 'main'
    AMAZON_BASE_URL = 'https://www.amazon.com'
    AMAZON_SEARCH_TERM = 'iphone 16 black 256 gb'
  }

  stages {
    stage('Checkout from GitHub') {
      steps {
        git branch: env.GITHUB_BRANCH, url: env.GITHUB_REPO_URL
      }
    }

    stage('Install Python dependencies') {
      steps {
        bat 'python -m pip install --upgrade pip'
        bat 'python -m pip install -r requirements.txt'
      }
    }

    stage('Install Playwright browser') {
      steps {
        bat 'python -m playwright install chromium'
      }
    }

    stage('Run Playwright tests') {
      steps {
        withCredentials([
          string(credentialsId: 'amazon-username', variable: 'AMAZON_USERNAME'),
          string(credentialsId: 'amazon-password', variable: 'AMAZON_PASSWORD')
        ]) {
          bat 'python -m pytest'
        }
      }
    }

    stage('Generate Allure report') {
      steps {
        bat 'allure generate allure-results --clean -o allure-report || exit 0'
      }
    }
  }

  post {
    always {
      archiveArtifacts artifacts: 'allure-report/**', allowEmptyArchive: true
    }
  }
}
