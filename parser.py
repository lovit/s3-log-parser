from collections import namedtuple
import csv

columns = 'owner bucket time remote_ip requester request_id operation key request_url http_status error_code bytes_sent object_size total_time turnaround_time referrer user_agent version_id'
class Log(namedtuple('Log', columns)):
    def __repr__(self):
        cols = ['  {} : {}'.format(key, value) for key, value in self._asdict().items()]
        strf = 'Log(\n{}\n)'.format('\n'.join(cols))
        return strf

def parse(line):
    """
    Arguments
    ---------
    line : str
        S3 access log

    Returns
    -------
    log : Log(namedtuple)
        Parsed log

    Usage
    -----

        >>> line = '1e28afdbd73**** bucket-name [05/Feb/2019:20:37:01 +0000] ***.***.***.*** 1e28afdbd73f*** F6425**** REST.HEAD.OBJECT directory/subdirectory/filename "HEAD /bucket-name/directory/subdirectory/filename HTTP/1.1" 200 - - 276913361 7 - "-" "aws-internal/3 aws-sdk-java/1.11.481 Linux/4.9.137-0.1.ac.218.74.329.metal1.x86_64 OpenJDK_64-Bit_Server_VM/25.192-b12 java/1.8.0_192" -'
        >>> parse(line)
    """

    line_ = line.replace('[', '"', 1).replace(']', '"', 1)
    return Log(*next(csv.reader([line_], delimiter=' ')))
