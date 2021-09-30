



jQuery(document).ready(function($){  
    $('#slow_nav  ul li').hover(
                function () {
                    $('ul', this).stop().slideDown(400);
                }, 
                function () {
                    $('ul', this).stop().slideUp(400);            
                }
            );
    $('#slow_nav_f  ul li').hover(
       
        function () {
            $('ul', this).stop().slideDown(400);
            }, 
        function () {
            $('ul', this).stop().slideUp(400);            
                }
            );
    

    let i = 0;

    // $('.circle__main__1').css('background', 'rgba(61, 29, 0, 0.33)');

    $('.main__arrow__scroll').on('click', function(){
        
        i++;
        let current = $('div.daily__markets__news').find('div.daily__news');
        
        let next = $('.daily__markets__news').find('div.active').next();
        let next__circle = $('.circle__main__page').find('div.active').next();

        let prev = $('.daily__markets__news').find('div.active').prev();
        $('.daily__markets__news').find('div.active').removeClass('active d-block').addClass('d-none');
        $('.circle__main__page').find('div.active').removeClass('active splash');
            if ( i <= current.length - 1 ) {
                
                next.addClass('active d-block');
                next__circle.addClass('active splash');
                // $('.circle__main__1').find('div.splash').css('background', '#3d1d00');
            }
           
            else {
                $('div.daily__markets__news').find('div.daily__news:first').addClass('active d-block');
                $('div.circle__main__page').find('div.circle__main__1:first').addClass('active splash');
                i=0;
            }
        return i;

        // circle__main__page
        //         circle__main__1    
    });
    $('#cima__1').on('click', function(){
        // $('#cima__1').addClass('d-none');
        $('div.daily__markets__news').find('div.daily__news').removeClass('active d-block').addClass('d-none');
        $('div.daily__markets__news').find('div.daily__news:first').addClass('active d-block');
        i = 0;
        $('div.circle__main__page').find('div.circle__main__1').removeClass('active splash');
        $('div.circle__main__page').find('div.circle__main__1:first').addClass('active splash');
        
        return i;
    });
    $('#cima__2').on('click', function(){
        // $('#cima__1').addClass('d-none');
        $('div.daily__markets__news').find('div.daily__news').removeClass('active d-block').addClass('d-none');
        $('div.daily__markets__news').find('div.daily__news:nth-child(2)').addClass('active d-block');
        i = 1;
        $('div.circle__main__page').find('div.circle__main__1').removeClass('active splash');
        $('div.circle__main__page').find('div.circle__main__1:nth-child(2)').addClass('active splash');
        return i;
    });
    $('#cima__3').on('click', function(){
        // $('#cima__1').addClass('d-none');
        $('div.daily__markets__news').find('div.daily__news').removeClass('active d-block').addClass('d-none');
        $('div.daily__markets__news').find('div.daily__news:nth-child(3)').addClass('active d-block');
        i = 2;
        $('div.circle__main__page').find('div.circle__main__1').removeClass('active splash');
        $('div.circle__main__page').find('div.circle__main__1:nth-child(3)').addClass('active splash');
        
        return i;
    });


    


});
jQuery(document).ready(function(){
    
});
    // SLICK slider
jQuery(document).ready(function(){ 
    let tickersForCompany = ['NASDAQ:TELL','NYSE:QD','NASDAQ:NOVN','NASDAQ:GNUS','NASDAQ:BKYI','NASDAQ:CVAC','NYSE:SOL','NYSE:GE','NYSE:TALO','NASDAQ:CLXT','NASDAQ:CODX','NASDAQ:HTGM','AMEX:INUV'] 
    $('.slider').slick({
        arrows:true,
        adaptiveHeight:true,
        slidesToShow:4,
        slidesToScroll:1,
        speed:1000,
        easing: 'ease',
        autoplay:true,
        autoplaySpeed:1500,
        pauseOnFocus:true,
        pauseOnHover:true,
        variableWidth:false,
        draggable:false,
        responsive:[
            {
                breakpoint:1000,
                setting: {
                    slidesToShow:1
                }
            }
            
        ]
    });
    
                
 });

// client portal 

let client_portal = $('#sign__client').html();
$('main').append(client_portal);


// Close Coments

$('#close__coments').on('click', function(){
    $('#coments__main').toggleClass('d-none');
    $('#coments__reply').toggleClass('d-none');
    $('#coments__').toggleClass('pb-4');
    $('#close__coments').find('img').toggleClass('rotated');
})

//

$('#btn__major1').on('click', function(){
    $('#major__page2').toggleClass('d-none');
    $('#major__page3').toggleClass('d-none');
    $('#major__main__page').toggleClass('h100vh');
});




// clear input
$('.input_1').click(function(){
    $(this).val('').change(); 
});


$(window).scroll(function(){
    var docscroll=$(document).scrollTop();
    if(docscroll>$(window).height()){
      $('.block__menu').addClass('fixed').css('display', 'none').removeClass('d-flex');
    }else{
      $('.block__menu').removeClass('fixed').addClass('d-flex');
    }
    $(document).mousemove(function(event){
        var y = event.clientY;
        if (y < 50) {
            $('.block__menu').css('display', 'flex');
            
        }
    });
      
  });
// asdasd

$('.button__darkgreen').mousemove(function(){
    $(this).find('.bg__color1').css('width','180px');
    $(this).find('.arrow__left').css('right','10px');
    $(this).find('div.ff__robo').css({position: "absolute",'z-index':9999});
    // $('.bg__color1').html('<p class="text-uppercase text-light p-2 m0p0 ff__robo">learn more</p>');
})

$('.button__darkgreen').mouseleave(function(){
    $(this).find('.arrow__left').css('right','-30px');
    $(this).find('.bg__color1').css('width','40px');
    $(this).find('div.ff__robo').css({position: "absolute",'z-index':6565});
})



document.addEventListener('DOMContentLoaded', function() {
    // Button dropmenu
    $('#checkbox1').click( function(){
        if($('#checkbox1').prop('checked')){
              $('.mob_menu').css('display', 'flex');
              $('.hamburger').css('position','fixed');
              $('.hamburger').css('margin-right','40px');
              $('main').css('filter','blur(11px)');
              $('body').css('overflow-y','hidden');
        }else{
            $('.mob_menu').css('display', 'none');
            $('.hamburger').css('position','absolute');
            $('main').css('filter','blur(0px)');
            $('body').css('overflow-y','scroll');
        }
       
    });

    // $('#close__coments').on('click', function(){
    //     $('#coments__mmain').css('display','none !important');
    // })

$(document).ready(function(){
    $('#button__client__portal').on('click', function(){
        if ($('#sign__up').hasClass('show') || $('#reset').hasClass('show')) {
            $('#daily__markets__news').css('display','none');
            $('#client__portal').css('display','block').addClass('show');
        
            // $('#main__block').css('filter','blur(11px)');


            $('#sign__up').css('display','none').removeClass('show');
            $('#reset').css('display','none').removeClass('show');
        }
        else {
            $('#daily__markets__news').css('display','none');
            $('#client__portal').css('display','block').addClass('show');
        
            // $('#main__block').css('filter','blur(11px)');
            
        }
        
    });

    $('#button__sign__up').on('click', function(){
        
        if ($('#client__portal').hasClass('show') || $('#reset').hasClass('show')) {
                $('#daily__markets__news').css('display','none');
                $('#sign__up').css('display','block').addClass('show');
                // $('#main__block').css('filter','blur(11px)');

               
                $('#client__portal').css('display','none').removeClass('show');
                $('#reset').css('display','none').removeClass('show');

        }
        else {
            $('#daily__markets__news').css('display','none');
            $('#sign__up').css('display','block').addClass('show');
            // $('#main__block').css('filter','blur(11px)');
        }
    });

    $('#button__reset').on('click', function(){

        if ($('#client__portal').hasClass('show') || $('#sign__up').hasClass('show')) {
                $('#daily__markets__news').css('display','none');
                $('#reset').css('display','block').addClass('show');
                // $('#main__block').css('filter','blur(11px)');


                $('#client__portal').css('display','none').removeClass('show');
                $('#sign__up').css('display','none').removeClass('show');

        }
        else {
            $('#daily__markets__news').css('display','none');
            $('#reset').css('display','block').addClass('show');
            // $('#main__block').css('filter','blur(11px)');
        }
    });

    $("#reset_submit").click(function (e) {
        e.preventDefault();
        $("#reset_submit").attr('disabled', true);
        $.ajax({
            type: 'post',
            url: '/resetpassword',
            data: $('#reset_form').serialize(),
                success: function (r) {
                    $(".text-danger.reset_p").html(r);
                    $("#email_reset").val('');
                    $("#reset_submit").attr('disabled', false)
                }
            })
    })



    $('#button_close_client_portal').on('click', function(){
        $('#client__portal').css('display','none').removeClass('show');
        $('#main__block').css('filter','blur(0px)');
        $('#daily__markets__news').css('display','flex'); 
    });
    
    $('#button_close_sign_up').on('click', function(){
        $('#sign__up').css('display','none');
        $('#main__block').css('filter','blur(0px)');
        $('#daily__markets__news').css('display','flex'); 
    });

    $('#button_close_reset_password').on('click', function(){
        $('#reset__password').css('display','none');
        $('#main__block').css('filter','blur(0px)');
        $('#daily__markets__news').css('display','flex');
    })
});


$('#list_1').addClass('animate__fadeIn animate__animated');
$('#button_1').click(function(e){

    if ($('#list_1').hasClass('d-block') == false){
        
        $('#spn1').text('-');
        $('#list_1').removeClass('animate__fadeOut');
        $('#list_1').addClass('animate__fadeIn');
        $('#list_1').toggleClass('d-block');
        $('#list_2').removeClass('d-block');
        $('#spn2').text('+');
        $('#list_3').removeClass('d-block');
        $('#spn3').text('+');
        $('#list_4').removeClass('d-block');
        $('#spn4').text('+'); 
        }
    else {
        
        $('#spn1').text('+');
        $('#list_1').removeClass('animate__fadeIn');
        $('#list_1').addClass('animate__fadeOut');
            setTimeout(function(){

                $('#list_1').toggleClass('d-block');
                
            },300);
    }
});
$('#button_2').click(function(e){

    if ($('#list_2').hasClass('d-block') == false){
        
        $('#spn2').text('-');
        $('#list_2').removeClass('animate__fadeOut');
        $('#list_2').addClass('animate__fadeIn');

        $('#list_2').toggleClass('d-block')
        $('#list_1').removeClass('d-block');
        $('#spn1').text('+');
        $('#list_3').removeClass('d-block');
        $('#spn3').text('+');
        $('#list_4').removeClass('d-block');
        $('#spn4').text('+');       
    }
    else {
        
        $('#spn2').text('+');
        $('#list_2').removeClass('animate__fadeIn');
        $('#list_2').addClass('animate__fadeOut');
        setTimeout(function(){

            $('#list_2').toggleClass('d-block');
                
        },300);
    }
});
$('#button_3').click(function(e){

    if ($('#list_3').hasClass('d-block') == false){
       
        $('#spn3').text('-');
        $('#list_3').removeClass('animate__fadeOut');
        $('#list_3').addClass('animate__fadeIn');

        $('#list_3').toggleClass('d-block');
        $('#list_2').removeClass('d-block');
        $('#spn2').text('+');
        $('#list_1').removeClass('d-block');
        $('#spn1').text('+');
        $('#list_4').removeClass('d-block');
        $('#spn4').text('+');      
    }
    else {
        
        $('#spn3').text('+');
        $('#list_3').removeClass('animate__fadeIn');
        $('#list_3').addClass('animate__fadeOut');
        setTimeout(function(){

            $('#list_3').toggleClass('d-block');
                
        },300);
    }
});
$('#button_4').click(function(e){

    if ($('#list_4').hasClass('d-block') == false ){
        
        $('#spn4').text('-');
        $('#list_4').removeClass('animate__fadeOut');
        $('#list_4').addClass('animate__fadeIn');

        $('#list_4').toggleClass('d-block')
        $('#list_2').removeClass('d-block');
        $('#spn2').text('+');
        $('#list_3').removeClass('d-block');
        $('#spn3').text('+');
        $('#list_1').removeClass('d-block');
        $('#spn1').text('+');      
    }
    else {
        
        $('#spn4').text('+');
        $('#list_4').removeClass('animate__fadeIn');
        $('#list_4').addClass('animate__fadeOut');
        setTimeout(function(){

            $('#list_4').toggleClass('d-block');
                
        },300);
    }
});
$('div.col-lg-1').click(function(){
    $('.carusel').each(function() {
        $(this).insertBefore($(this).prev());
      });
});

// 2.0
$('#search__link').on('click', function (){
    $('.input__search').toggleClass('block__visib');
});


// $(document).ready(function(){
//     var market = [];
//     var v = [];
//     var x = $('.market__news__item');

//     for(var i=0; i <= x.length; i++  ) {
//         market.push(x[i]);
//     }

//     var reverse = market.reverse();
//     // var reverse = market.reverse();
//     // v =+ market.reverse();
//     console.log(Array.isArray(market));
//     console.log(reverse);
// }); 


// button large__GRAFF
$('#butt__large__graff').on('click', function(){
    $('#main__price__chart').addClass('d-lg-none');
    $('#large__graff').toggleClass('d-lg-none');
});

//PORTFOLIO CHART 
$('#arrow__top__portfolio').on('click', function(){
    $('#portfolio__chart').toggleClass('d-lg-none');
    $('#portfolio__table').toggleClass('portfolio__table');
    $('#arrow__top__portfolio').find('img').toggleClass('rotated');
})





// button portfolio
$('#button__submit__portfolio').on('click',function(){
    metaDate = { 
        symbols: $('#symbols__port').val(),
        csrf_token: $('#csrf').val()
    }
    $.post( "/portfolio", metaDate);
});

$(".button_com_like").unbind('click').click(function(e) {
    e.preventDefault();
    let com_id = $(this).attr('data-id'),
        csrf = $("[name='csrf_token']").val(),
        elem = $(this);
    $.post('/likee', {comment_id: com_id, csrf_token: csrf}, function(r) {
        if (typeof r == 'object') {
            elem.find('i').toggleClass('far fas', 'fas far')
            $("[data-like='" + com_id + "']").html(r['like_count'])
        } else {
            alert(r)
        }
    })
})

$( "#forms__coment" ).on( "submit", function( event ) {
    event.preventDefault();
    formDate = $( "#forms__coment" ).serialize();
        $.post('/stocks/jyforum', formDate).done(function(){
            alert('Your comment add to board');
            location.reload();
        })
        
    
  });


});
