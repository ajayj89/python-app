
Basic Python App to deploy the apis with errors, positive and few flows.
If server runs in local, following are the apis :

    http://127.0.0.1:8080/hello. --> Positive api hit
    http://127.0.0.1:8080/error-500. --> throws 500 internal server error
    http://127.0.0.1:8080/error-502. --> throws 502  bad gateway


Start load on server after deployment:

    nohup sh gen-load.sh python-pve.bugbash.tpe 600 > sm-sm20.out 2>&1 &

    where; $1 is host, $2 is duration (in sec)
