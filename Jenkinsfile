node {
    // This displays colors using the 'xterm' ansi color map.
        stage('checkout') {
          checkout scm
        }
        stage('build') {
          sh 'zip pythonscript.zip app.py util.py'
        }
        stage('deploy') {
          sh 'aws s3api createbucket --bucket sample-bucket --region us-east-1'
	  sh 'aws s3 cp pythonscript.zip s3://sample-bucket/'
        }
}
