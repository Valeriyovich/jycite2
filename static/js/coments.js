var $form =  $('.form_request_coment');
$form.hide();
var flag = true;
$('.button_coment').click(function(){       
    $form.hide(); 
    $('.button_coment').text('reply'); 
    if(!$(this).hasClass('active')){         
        $(this).text('close').addClass('active');
        var $comment =  $(this).parent().parent();
        $form.find('#hidden_input_request').val($comment.attr('id'));
        $form.find('.send_reply').attr('id', 'butt'+$comment.attr('id'));
        $comment.append($('.form_request_coment').show());
    }
    else{
        $('.button_coment').removeClass('active');  
    }
});

var all_message = $('#all_messages');

$('#all_messages').on('click', '.like', function(e) {
    var parent =  $(this).parent();
    var count = 0 ;
    var parent_text = parseInt(parent.find($('.count')).text());
    console.log(parent_text);
    if ($(this).hasClass('liked') == true) {
        $(this).removeClass('liked');
        $(this).removeClass('bg-danger');
        count -= 1;
        parent_text = parent_text + count;
        parent.find($('.count')).text(parent_text);
    }
    else {
        count += 1;
        $(this).addClass('liked');
        $(this).addClass('bg-danger');
        parent_text = parent_text + count;
        console.log(parent_text);
        parent.find($('.count')).text(parent_text);
    }
    // console.log($(this).data('id'));
    // console.log($(this).parent());
});
async function allLikee(url) {
    try {
        const response = await fetch(url);
        const data = await response.json();
        var likee = data;
        console.log(likee);
        // const countries = countries1.map((item,index)=>item=item+' | '+countries2[index]);
    }
    catch(err) {
        console.log(err);
    }
}
console.log('asdasd')
jQuery(document).ready(function(){
    allLikee('/likee');
});


// $('#buttons_block').append('<form class="input_coment d-flex p-3" method="POST"><input class="m0p0" style="width:calc(100% - 24px)"> <button class="border" >ok</button><form>');