pipeline {
  agent any
  triggers {
    pollSCM('H/15 * * * *')
  }
  stages {
    stage('Build Container') {
      agent {
        label "Pi_Zero"
      }
      steps {
        sh "docker build -t dht22 ."
      }
    }
    stage('Tag Container') {
      agent {
        label "Pi_Zero"
      }
      steps {
        sh "docker tag dht22 fx8350:5000/dht22:latest"
        sh "docker tag dht22 fx8350:5000/dht22:${env.BUILD_NUMBER}"
        sh "docker tag dht22 leonhess/dht22:latest"
        sh "docker tag dht22 leonhess/dht22:${env.BUILD_NUMBER}"
      }
    }
    stage('Push to Registries') {
      parallel {
        stage('Push to local Registry') {
          agent {
            label "Pi_Zero"
          }
          steps {
            sh "docker push fx8350:5000/dht22:${env.BUILD_NUMBER}"
            sh "docker push fx8350:5000/dht22:latest"
          }
        }
        stage('Push to DockerHub') {
          agent {
            label "Pi_Zero"
          }
          steps {
            withDockerRegistry([credentialsId: "dockerhub", url: ""]) {
              sh "docker push leonhess/dht22:${env.BUILD_NUMBER}"
              sh "docker push leonhess/dht22:latest"
            }
          }
        }
      }
    }
    stage('Cleanup') {
      agent {
        label "Pi_Zero"
      }
      steps {
        sh "docker rmi -f dht22"
        sh "docker rmi -f fx8350:5000/dht22:latest"
        sh "docker rmi -f fx8350:5000/dht22:${env.BUILD_NUMBER}"
        sh "docker rmi -f leonhess/dht22:latest"
        sh "docker rmi -f leonhess/dht22:${env.BUILD_NUMBER}"
      }
    }
    stage('Deploy') {
      agent {
        label "master"
      }
      steps {
        ansiblePlaybook(
          playbook: 'deploy.yml',
          credentialsId: 'd36bc821-dad8-45f5-9afc-543f7fe483ad'
          )
        }
      }
    }
  }
