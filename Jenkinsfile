pipeline {
agent { label 'gcp' }
environment {
		POSTGRES_DB = credentials('POSTGRES_DB')
		POSTGRES_USER = credentials('POSTGRES_USER')
		POSTGRES_PASSWORD = credentials('POSTGRES_PASSWORD')
		POSTGRES_TEST_DB = credentials('POSTGRES_TEST_DB')
		POSTGRES_TEST_DB_USER = credentials('POSTGRES_TEST_DB_USER')
		POSTGRES_TEST_DB_PASSWORD = credentials('POSTGRES_TEST_DB_PASSWORD')
    }
stages {
	stage('Build Docker Image') {
	steps {
		sh '''
			sudo docker-compose --build-arg POSTGRES_DB='$POSTGRES_DB' --build-arg POSTGRES_PASSWORD='$POSTGRES_PASSWORD' --build-arg POSTGRES_USER='$POSTGRES_USER' --build-arg POSTGRES_TEST_DB='$POSTGRES_TEST_DB' --build-arg POSTGRES_TEST_DB_PASSWORD='$POSTGRES_TEST_DB_PASSWORD' --build-arg POSTGRES_TEST_DB_USER='$POSTGRES_TEST_DB_USER' --detach --verbose
			sudo docker-compose up -d
		'''
	}
	}
	stage ('Launch Test environment') {
	steps {
			sh '''
			    export FLASK_APP="app:create_app('testing')"
				flask run --host=0.0.0.0
			'''
		}
		}
	stage('Test') {
	steps {
		sh 'pytest'
		input(id: "Deploy Gate", message: "Deploy ${params.project_name}?", ok: 'Deploy')
	}
	}

	stage('Deploy') {
	steps {
		echo "deploying the application"
		sh '''
			export FLASK_APP="app:create_app('development')"
			flask run --host=0.0.0.0 > log.txt 2>&1 &
		'''
	}
	}
}

post {
		always {
			echo 'The pipeline completed'
			junit allowEmptyResults: true, testResults:'**/test_reports/*.xml'
		}
		success {				
			echo "Flask Application Up and running!!"
		}
		failure {
			echo 'Build stage failed'
			error('Stopping early…')
		}
	}
}
