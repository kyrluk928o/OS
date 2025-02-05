pipeline {
    agent {
        docker {
            image 'my-jenkins'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    stages {
        stage('Clone repository') {
            steps {
                git branch: 'main', url: 'https://github.com/kyrluk928o/OS'
            }
        }
        stage('Download DEB package') {
            steps {
                sh '''
                    curl -L https://github.com/kyrluk928o/OS/blob/main/count-file_1.0-1.deb -o /tmp/count-file_1.0-1.deb
                '''
            }
        }
        stage('Install DEB') {
            steps {
                sh '''
                    sudo dpkg -i /tmp/count-file_1.0-1.deb
                '''
            }
        }
        stage('Download script') {
            steps {
                sh '''
                    curl -L https://github.com/kyrluk928o/OS/blob/main/count_files.sh -o /tmp/count_files.sh
                    chmod +x /tmp/count_files.sh
                '''
            }
        }
        stage('Run script') {
            steps {
                sh '/tmp/count_files.sh'
            }
        }
    }
}
