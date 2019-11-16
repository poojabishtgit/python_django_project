// alert()
$(document).ready(()=>{
    $("#btnregister").click(()=>{
        // alert()
        FormData = $("#register-form").serialize()
        // alert("FormData")
        $.ajax({
            data: FormData,
            url: "register",
            type: "post",
            success: function(response){
                $("#error").html(response)
                if (response == 'Register Successfully')
                {
                    $("login-form-link").trigger('click')
                } 
            }
        })
    })
})