pipeline {
  agent any
  stages {
    stage('Deploy') {
      steps {
        publishOverSsh {
            server('minecraft-server') {
                transferSet {
                    sourceFiles('file')
                }
            }
        }
      }
    }
  }
}
