BEGIN {
    nrows=0
    tdate=""
    tdesc=""
    tamt=0

}

{

    if($1=="TRANSACTION") {
        print $0
        nrows=0
    }
    if(nrows==1) {
        tdate=$1
        tdesc=$2
    } else if(nrows==2) {
    } else if(nrows==3) {
    } else if(nrows==4) {
        print $tdate "\t" tdesc "\t" tamt

    }
    if($1!="ELIGIBLE") nrows++
} 

