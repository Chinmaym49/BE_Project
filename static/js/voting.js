$(document).ready(function() {

    var submitActor=null;
    var $submitActors=$("#all_ans").find("button[name='vote']");

    $("#all_ans").on("submit",function(event) {
        $.ajax({
            data: {
                aid_f:submitActor.value
            },
            type:"POST",
            url:"/vote"
        })
        .done(function(data) {
            console.log(data);
            $(data["ui"]).css("background-color",data["uc"]);
            $(data["di"]).css("background-color",data["dc"]);
            var v=eval($(data["vi"]).text().trim()+data["v"]);
            $(data["vi"]).html(v);
        });
        event.preventDefault();
    });

    $submitActors.click(function(event) {
        submitActor = this;
    });

});