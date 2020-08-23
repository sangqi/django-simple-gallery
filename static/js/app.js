$(document).ready(function () {
    $('[data-toggle="tooltip"]').tooltip();

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                // Only send the token to relative URLs i.e. locally.
                xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
            }
        }
   });

    $('#photoDetailLikeImage').on('click', function () {
        create_like.call(this, like_success_callback, general_error_callback);
    });
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?

            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

/* Likes */
function create_like(success_callback, error_callback) {
    var photo_pk = $('#photoDetailHiddenId').text();

    $.ajax({
        type: 'POST',
        url: '/photo/like/',
        data: {
            photo_pk: photo_pk
        },
        success: function (data) { success_callback(data); },
        error: function (error) { error_callback(error); }
    });
}

function like_success_callback(data) {
    if (data.liked) {
        $('#photoDetailLikeImage').removeClass('far').addClass('fas');
    } else {
        $('#photoDetailLikeImage').removeClass('fas').addClass('far');
    }

    var text = '';
    if (data.like_count <= 1) {
        text = data.like_count + ' like';
    } else {
        text = data.like_count + ' likes';
    }

    if (data.liked) {
        text += ' (Already liked)';
    }

    $('#photoDetailLikeText').text(text);
}

function general_error_callback(error) {
    console.log(error)
}
