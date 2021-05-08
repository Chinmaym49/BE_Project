let vote=(id)=> {
    let green="rgb(76, 175, 80)";
    let red="rgb(244, 67, 54)";
    let white="rgb(239, 239, 239)";
    let aid=id.split("_")[0];
    let v=aid+"_v";
    let idu=aid+"_up";
    let idd=aid+"_down";
    let stat="";
    
    let cu=document.getElementById(idu).style.backgroundColor;
    let cd=document.getElementById(idd).style.backgroundColor;
    
    if(cu==green) {
        stat=1;
    } else if(cd==red) {
        stat=-1;
    } else {
        stat=0;
    }

    if(id.includes("up")) {
        if(stat==0) {
            stat=1;
            document.getElementById(idu).style.backgroundColor=green;
            document.getElementById(v).innerHTML=1+parseInt(document.getElementById(v).innerHTML);
        } else if(stat==1) {
            stat=0;
            document.getElementById(idu).style.backgroundColor=white;
            document.getElementById(v).innerHTML=-1+parseInt(document.getElementById(v).innerHTML);
        } else {
            stat=1;
            document.getElementById(idu).style.backgroundColor=green;
            document.getElementById(idd).style.backgroundColor=white;
            document.getElementById(v).innerHTML=2+parseInt(document.getElementById(v).innerHTML);
        }
    } else {
        if(stat==0) {
            stat=-1;
            document.getElementById(idd).style.backgroundColor=red;
            document.getElementById(v).innerHTML=-1+parseInt(document.getElementById(v).innerHTML);
        } else if(stat==-1) {
            stat=0;
            document.getElementById(idd).style.backgroundColor=white;
            document.getElementById(v).innerHTML=1+parseInt(document.getElementById(v).innerHTML);
        } else {
            stat=-1;
            document.getElementById(idu).style.backgroundColor=white;
            document.getElementById(idd).style.backgroundColor=red;
            document.getElementById(v).innerHTML=-2+parseInt(document.getElementById(v).innerHTML);
        }
    }
    
    let payload=JSON.stringify({aid_f:id});
    fetch("/vote",{
        method: "POST",
        body: payload
    })
    .then((resp)=>(resp.json()))
    .then((data)=>(console.log(data.status)))
    .catch((err)=>(alert("An error occured!")));
};