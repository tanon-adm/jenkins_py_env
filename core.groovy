firstFail = true

def Test() {
    //marker = true
}

def fail() {
    try {
            error("TestError")
        }
    } catch(e) {
        echo "Generating NuGet packages failed: ${e}"
        failBuild()
        throw e
    }
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
