$(function() {
    'use strict';

    $('#id_contact_form').on('submit', function() {
        var post_url = $("#id_contact_form").data("post-url");

        var formData = new FormData(this);

        $.ajax({
            url : post_url,
            type: "POST",
            data : formData,
            processData: false,
            contentType: false,
            success:function(response){
                var message = response.content.message
                alert(message);
            },
        });

        return false;
    });
});