// alert()
$(document).ready(()=>{
    $("#btnregister").click(()=>{
        // alert()
        FormData = $("#reg-form").serialize()
        // alert("FormData")
        $.ajax({
            data: FormData,
            url: "/register",
            type: "post",
            success: function(responce){

            }

        })
    })
})