package com.mirantis.mk

/**
 *
 * Git functions
 *
 */

/**
 * Checkout single git repository
 *
 * @param path            Directory to checkout repository to
 * @param url             Source Git repository URL
 * @param branch          Source Git repository branch
 * @param credentialsId   Credentials ID to use for source Git
 * @param poll            Enable git polling (default true)
 * @param timeout         Set checkout timeout (default 10)
 * @param depth           Git depth param (default 0 means no depth)
 * @param reference       Git reference param to checkout (default empyt, i.e. no reference)
 */
def checkoutGitRepository(path, url, branch, credentialsId = null, poll = true, timeout = 10, depth = 0, reference = ''){
    def branch_name = reference ? 'FETCH_HEAD' : "*/${branch}"
    dir(path) {
        checkout(
            changelog:true,
            poll: poll,
            scm: [
                $class: 'GitSCM',
                branches: [[name: branch_name]],
            doGenerateSubmoduleConfigurations: false,
            extensions: [
                [$class: 'CheckoutOption', timeout: timeout],
                [$class: 'CloneOption', depth: depth, noTags: false, shallow: depth > 0, timeout: timeout]],
            submoduleCfg: [],
            userRemoteConfigs: [[url: url, credentialsId: credentialsId, refspec: reference]]]
        )
        sh(returnStdout: true, script: 'git rev-parse HEAD').trim()
    }
}