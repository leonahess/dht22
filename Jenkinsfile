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
    stage('Update main GitHub repo') {
      agent {
        label 'master'
      }
      steps {
        sh "git clone git@github.com:leonhess/smarthome.git /tmp"
        sh "cd smarthome"
        sh "git submodule update --init --remote"
        sh "git add --a"
        sh "git commit -m 'updated dht22 submodule'"
        sh "git push"
        sh "rm -rf /tmp/smarthome"
      }
    }
    stage('Deploy') {
      parallel {
        stage('Deploy to leon-pi-zero-1') {
          agent {
            label "master"
          }
          steps {
            sshagent(credentials: ['d36bc821-dad8-45f5-9afc-543f7fe483ad']) {
              sh "ssh -o StrictHostKeyChecking=no pirate@leon-pi-zero-1 docker kill dht22"
              sh "ssh -o StrictHostKeyChecking=no pirate@leon-pi-zero-1 docker rm dht22"
              sh "ssh -o StrictHostKeyChecking=no pirate@leon-pi-zero-1 docker run --restart always -d --name=dht22 --privileged fx8350:5000/dht22:latest"
            }
          }
        }
        stage('Deploy to leon-pi-zero-2') {
          agent {
            label 'master'
          }
          steps {
            sshagent(credentials: ['d36bc821-dad8-45f5-9afc-543f7fe483ad']) {
              sh "ssh -o StrictHostKeyChecking=no pirate@leon-pi-zero-2 docker kill dht22"
              sh "ssh -o StrictHostKeyChecking=no pirate@leon-pi-zero-2 docker rm dht22"
              sh "ssh -o StrictHostKeyChecking=no pirate@leon-pi-zero-2 docker run --restart always -d --name=dht22 --privileged fx8350:5000/dht22:latest"
            }
          }
        }
      }
    }
  }
}
