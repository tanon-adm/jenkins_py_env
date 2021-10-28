def firstFail = true

def Test() {
    //marker = true
}

def failBuild() {
    currentBuild.result = 'FAILURE'
    if (firstFail) {
        currentBuild.description = "Failed in stage \"${STAGE_NAME}\""
        firstFail = false
    }
}

// Do not remove this line. It is used for importing the file into the Jenkinsfile.
return this
