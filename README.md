# S3 bucket access log parser

```python
from parser import parse

log_line = '1e28afdbd73**** bucket-name [05/Feb/2019:20:37:01 +0000] ***.***.***.*** 1e28afdbd73f*** F6425**** REST.HEAD.OBJECT directory/subdirectory/filename "HEAD /bucket-name/directory/subdirectory/filename HTTP/1.1" 200 - - 276913361 7 - "-" "aws-internal/3 aws-sdk-java/1.11.481 Linux/4.9.137-0.1.ac.218.74.329.metal1.x86_64 OpenJDK_64-Bit_Server_VM/25.192-b12 java/1.8.0_192" -'

parse(log_line)
```

```
Log(
  owner : 1e28afdbd73****
  bucket : bucket-name
  time : 05/Feb/2019:20:37:01 +0000
  remote_ip : ***.***.***.***
  requester : 1e28afdbd73f***
  request_id : F6425****
  operation : REST.HEAD.OBJECT
  key : directory/subdirectory/filename
  request_url : HEAD /bucket-name/directory/subdirectory/filename HTTP/1.1
  http_status : 200
  error_code : -
  bytes_sent : -
  object_size : 276913361
  total_time : 7
  turnaround_time : -
  referrer : -
  user_agent : aws-internal/3 aws-sdk-java/1.11.481 Linux/4.9.137-0.1.ac.218.74.329.metal1.x86_64 OpenJDK_64-Bit_Server_VM/25.192-b12 java/1.8.0_192
  version_id : -
)
```