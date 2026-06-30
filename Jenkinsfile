pipeline {
  agent any

  environment {
    AMAZON_BASE_URL = 'https://www.amazon.com'
    AMAZON_SEARCH_TERM = 'iphone 16 black 256 gb'
  }

  stages {
    stage('Install dependencies') {
      steps {
        sh 'npm ci'
      }
    }

    stage('Install Playwright browsers') {
      steps {
        sh 'npx playwright install --with-deps chromium'
      }
    }

    stage('Run Playwright tests') {
      steps {
        withCredentials([
          string(credentialsId: 'amazon-username', variable: 'AMAZON_USERNAME'),
          string(credentialsId: 'amazon-password', variable: 'AMAZON_PASSWORD')
        ]) {
          sh 'npx playwright test'
        }
      }
    }

    stage('Generate Allure report') {
      steps {
        sh 'npx allure generate allure-results --clean -o allure-report || true'
      }
    }
  }

  post {
    always {
      archiveArtifacts artifacts: 'allure-report/**', allowEmptyArchive: true
    }
  }
}
