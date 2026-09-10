# Executing scripts locally

Scripts can be executed locally, though connections to databases, mail servers, LDAP, and other external systems may not be available in this environment.

For instance, create a lib directory somewhere on the disk and copy the following dependencies. Use whatever katl-commons dependency you have available

![Power Scripts for Jira Cloud local script execution environment](/cms_trial/assets/f46ff00b-9052-4549-af18-d6358a053681.png)

Now we can create a shell script so we can run SIL files, for instance for my Linux box, can save the `runsil.sh` as:

```shell
#!/bin/bash

BASEDIR=$(dirname -- "$(readlink -f "${BASH_SOURCE[0]}")")

jv=$(java -version 2>&1 | grep version | awk '{print $3;}')
if [[ $jv == \"1.8* ]]; then
  export JAVA_HOME=/opt/jdk/jdk-11
  export PATH=$JAVA_HOME/bin:$PATH
  echo "Java home set to: $JAVA_HOME"
fi

if [ ! -f "$BASEDIR/classpath_file" ]
then
  echo "com.keplerrominfo.sil.LangEngine" > "$BASEDIR/main-class-file"
  echo -n "." > "$BASEDIR/classpath_file"
  for f in "$BASEDIR"/lib/*.jar
  do
    echo -n ":$f" >> "$BASEDIR/classpath_file"
  done
fi  
#
# Assumes the java 11 home is set and the path is ok, see above
#
java -cp @"$BASEDIR"/classpath_file @"$BASEDIR"/main-class-file "$1" "$2"
```

Running it is easy:

```text
$ ./runsil.sh ./myprogram.sil param1
```

If you have webhooks on your server, you may invoke them from the local script. In this way you have a very powerful CLI solution at your fingertips.