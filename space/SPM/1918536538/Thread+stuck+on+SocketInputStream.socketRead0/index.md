# Thread stuck on SocketInputStream.socketRead0

## Symptoms

- Threads are timeouts waiting for a lock
- DB's connections are held for a long time and there are exceptions on retrieving new connections - the pool is exhausted.

## Problem identification

To properly identify a problem, thread dumps should be taken when it occurs. It is also possible to spot a problem after the first symptoms were seen, as threads might be stuck indefinitely.

- See: Gathering thread dumps: [Technical info page](https://appfire.atlassian.net/wiki/spaces/DLP/pages/297571655)

Sample thread dump with a stuck thread looks as follows:

```text
"SP-bigpicture-0000000.TaskSyncSingleJobExecutor-2791" prio=5 tid=0x0000000000000ae7 nid=0 runnable 
java.lang.Thread.State: RUNNABLE
at java.base@11.0.15/java.net.SocketInputStream.socketRead0(Native Method)
at java.base@11.0.15/java.net.SocketInputStream.socketRead(SocketInputStream.java:115)
at java.base@11.0.15/java.net.SocketInputStream.read(SocketInputStream.java:168)
at java.base@11.0.15/java.net.SocketInputStream.read(SocketInputStream.java:140)
at java.base@11.0.15/sun.security.ssl.SSLSocketInputRecord.read(SSLSocketInputRecord.java:478)
at java.base@11.0.15/sun.security.ssl.SSLSocketInputRecord.readHeader(SSLSocketInputRecord.java:472)
at java.base@11.0.15/sun.security.ssl.SSLSocketInputRecord.bytesInCompletePacket(SSLSocketInputRecord.java:70)
at java.base@11.0.15/sun.security.ssl.SSLSocketImpl.readApplicationRecord(SSLSocketImpl.java:1454)
at java.base@11.0.15/sun.security.ssl.SSLSocketImpl$AppInputStream.read(SSLSocketImpl.java:1065)
at org.postgresql.core.VisibleBufferedInputStream.readMore(VisibleBufferedInputStream.java:161)
at org.postgresql.core.VisibleBufferedInputStream.ensureBytes(VisibleBufferedInputStream.java:128)
at org.postgresql.core.VisibleBufferedInputStream.ensureBytes(VisibleBufferedInputStream.java:113)
at org.postgresql.core.VisibleBufferedInputStream.read(VisibleBufferedInputStream.java:73)
at org.postgresql.core.PGStream.receiveChar(PGStream.java:443)
at org.postgresql.core.v3.QueryExecutorImpl.processResults(QueryExecutorImpl.java:2069)
at org.postgresql.core.v3.QueryExecutorImpl.execute(QueryExecutorImpl.java:322)

 - locked <0x000000001880e144> (a org.postgresql.core.v3.QueryExecutorImpl)
at org.postgresql.jdbc.PgStatement.executeInternal(PgStatement.java:481)
at org.postgresql.jdbc.PgStatement.execute(PgStatement.java:401)
at org.postgresql.jdbc.PgPreparedStatement.executeWithFlags(PgPreparedStatement.java:164)
at org.postgresql.jdbc.PgPreparedStatement.executeQuery(PgPreparedStatement.java:114)
at org.apache.commons.dbcp2.DelegatingPreparedStatement.executeQuery(DelegatingPreparedStatement.java:83)
at org.apache.commons.dbcp2.DelegatingPreparedStatement.executeQuery(DelegatingPreparedStatement.java:83)
```

If a few consecutive thread dumps (separated by several seconds) contain the same thread in the RUNNABLE state at the SocketInputStream.socketRead0 method, the problem has been identified.

## Resolution

This is a network problem with a broken connection between Jira and the Database. While connections are expected to break, some network setups may inhibit information about one end of the connection breaking being passed to the other end.   
It has been identified that some proxies between Jira and Database might still keep the Jira socket open. This socket, not knowing that the database on the other end is no longer available, may keep waiting to receive the last bytes of data infinitely.   
  
Atlassian is aware of the problem and proposes a solution:   
<https://confluence.atlassian.com/jirakb/connection-problems-to-postgresql-result-in-stuck-threads-in-jira-1047534091.html>  
This may not work for newer Jira versions.   
  
To solve the problem, one may:

- identify proxy that is not closing open socket and further investigate the reason, fixing the problem in network connectivity
- contact Atlassian for further help as Jira is maintaining the connection pool to the database.