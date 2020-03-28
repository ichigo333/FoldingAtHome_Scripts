# FoldingAtHome_Scripts
 
Script for parsing output from Folding@Home logs.  The script will get information from Folding@Home API to see if WU was accepted and display awarded points.  For now, script assumes that you are providing a file containing "Sending" lines from the logs.  For example:

```
02:53:36:WU01:FS01:Sending unit results: id:01 state:SEND error:NO_ERROR project:13851 run:0 clone:12970 gen:8 core:0xa7 unit:0x00000009287234c95e730209fdfd2b00
```

Easiest way to get these lines on Linux is to do 

`cat * | grep 'Sending'`

in logs directory.  Please don't forget that current log.txt is outside of log directory. On Windows, use Notepad++ or similar to find all instances `Sending`.  Please note that you will have to filter out duplicates for now.  If WU fails to upload, there will be multiple instances of `Sending` line for a particular WU.

---

## Config

Config has 2 values `path` and `user`.  Path is the path to your file you want to parse and the user is your Folding@Home user. 

## Requirements

- Python3
- requests lib

## Sample output

Format of the output is: {project},{run},{clone},{gen},{unit},{code},{credit},{credit_time},{days},{cpuid}

```
13851,0,12970,8,0x00000009287234c95e730209fdfd2b00,Ok,1000,2020-03-24 03:02:55,0.0761,258795EECB272DD
11746,0,187,12,0x000000158ca304f15e62d603338a30e3,Ok,16615,2020-03-24 11:05:22,0.2648,158795EECB272DD
11778,0,22259,0,0x00000001287234c95e7748df5ff094d4,Ok,9405,2020-03-24 13:11:20,0.1358,158795EECB272DD
14533,0,3376,7,0x0000000980fccb025e72f2171ab6d004,,,,,
14533,0,1746,5,0x0000000a80fccb025e72f1fb5803c089,,,,,
```

Note that the last 2 WUs are missing in the API so we are unalbe to get information about them.  Seems to be an issue with API, or possibly the WUs aren't counted yet?