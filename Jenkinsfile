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
        sh "docker build -t hs110 ."
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
    stage('Cleanup') {
      agent {
        label "Pi_Zero"
      }
      steps {
        sh "docker rmi fx8350:5000/dht22:latest"
        sh "docker rmi fx8350:5000/dht22:${env.BUILD_NUMBER}"
        sh "docker rmi leonhess/dht22:latest"
        sh "docker rmi leonhess/dht22:${env.BUILD_NUMBER}"
      }
    }
    stage('Deploy') {
      steps {
        sshagent(credentials: ['6dc73e77-76d4-4af1-86f7-f37c15c78533']) {
          sh "ssh -o StrictHostKeyChecking=no leon-pi-zero-1"
          sh "docker kill dht22"
          sh "docker rm dht22"
          sh "docker run --net=host --restart always -d --name=hs110 fx8350:5000/dht22:latest"
        }
      }
    }
  }
}
