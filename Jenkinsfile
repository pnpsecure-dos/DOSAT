pipeline {
  agent none
  stages {
    stage('TC Allow Parallel Test') {
      parallel {
        stage('TC Allow Test_CentOS7.8') {
          steps {
            build 'TC Allow Test_CentOS7.8'
          }
        }

        stage('TC Allow Test_Win2016') {
          steps {
            build 'TC Allow Test_Win2016'
          }
        }

      }
    }

    stage('TC Deny Parallel Test') {
      parallel {
        stage('TC Allow Test_CentOS7.8') {
          steps {
            build 'TC Deny Test_CentOS7.8'
          }
        }

        stage('TC Deny Test_Win2016') {
          steps {
            build 'TC Deny Test_Win2016'
          }
        }

      }
    }

  }
}