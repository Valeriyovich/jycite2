var dict = {
    en: {
        'SITE-TITLE': 'Site title',
        'HEADING-ONE': 'Heading 1',
        'SOME-TEXT': 'Some text in tag P',
        'ANOTHER-TEXT': 'another text1',
        'HOME': 'HOME',
        'MARKETS': 'markets',
        'MARKET_NEWS': 'market news',
        'TRADING_CALENDAR': 'Trading calendar',
        'STOCKS': 'Stocks',
        'COMMODITIES': 'Commodities',
        'CURRENCIES': 'Currencies',
        'SERVICES': 'services',
        'LONG_TERM_INV': 'Long-term investing',
        'NEWS': 'news',
        'LOGIN': 'login',
        'CLIENT_PORTAL': 'client portal',
        'SIGN_UP': 'sign up',
        'DISCOVER_WORLD': 'discover world of opporutnities',
        'MORE_TEXT_1': 'Invest globally in stocks, options, futures, forex bonds and funds from a single integrated. Fund your account in multiple currencies and trade assets denominated in multiple currencies.Access market data 24 hours a day and six days a week',
        'MORE_TEXT_2': 'Invest globally in stocks, options, futures, forex bonds and funds from a single integrated. Fund your account in multiple currencies and trade assets denominated in multiple currencies.Access market data 24 hours a day and six days a week',
        'MORE_TEXT_3': 'Invest globally in stocks, options, futures, forex bonds and funds from a single integrated. Fund your account in multiple currencies and trade assets denominated in multiple currencies.Access market data 24 hours a day and six days a week',
        'CONTACT': 'contact',
        'SEND': 'send',
        'WORLD_NEWS': 'world news',
        'FORGOT_PASS': 'Forgot password? Click',
        'HERE': 'here',
        'RESSET_PASS': 'resset password'


    },
    ru: {
        'SITE-TITLE': 'Заголовок сайта',
        'HEADING-ONE': 'Заголовок первый',
        'SOME-TEXT': 'Какой то текст в теге P',
        'ANOTHER-TEXT': 'Другой текст',
        'HOME': 'ГЛАВНАЯ',
        'MARKETS': 'котировки',
        'MARKET_NEWS': 'НОВОСТИ РЫНКА',
        'TRADING_CALENDAR': 'ТОРГОВЫЙ КАЛЕНДАРЬ',
        'STOCKS': 'АКЦИИ',
        'COMMODITIES': 'СЫРЬЁ',
        'CURRENCIES': 'ВАЛЮТЫ',
        'SERVICES': 'СЕРВИСЫ',
        'WORLD_NEWS': 'мировые новости',
        'LONG_TERM_INV': 'долгосрочное инвестирование',
        'NEWS': 'новости',
        'LOGIN': 'вход',
        'CLIENT_PORTAL': 'личный кабинет',
        'SIGN_UP': 'регистрация',
        'DISCOVER_WORLD': 'открой мир возможностей',
        'MORE_TEXT_1': 'Глобально инвестируйте в акции, опционы, фьючерсы, валютные облигации и фонды из единой интегрированной системы. Пополняйте свой счет в нескольких валютах и ​​торгуйте активами номинированными в нескольких валютах Доступ к рыночным данным 24 часа в сутки и шесть дней в неделю',
        'MORE_TEXT_2': 'Глобально инвестируйте в акции, опционы, фьючерсы, валютные облигации и фонды с единого интегрированного счета. Пополняйте свой счет в нескольких валютах и ​​торгуйте активами в нескольких валютах. Доступ к рыночным данным 24 часа в сутки и шесть дней в неделю.',
        'MORE_TEXT_3': '',
        'CONTACT': 'связь',
        'SEND': 'отправить',
        'FORGOT_PASS': 'забыли пароль? жми',
        'HERE': 'ТУТ',
        'RESSET_PASS': 'сбросить пароль'   
    }
};
$.html5Translate = function(dict, lang){
    
    $('[data-translate-key]').each(function(){
        $(this).html( dict[ lang ][ $(this).data('translateKey') ] );
    });
    
};

$('a#translate_en').click(function(){
    $(document).ready(function(){
        $.html5Translate(dict, 'en');
    });
    $('span.change_txt').text('EN');
    localStorage.clear();
    $('#change1').css('display', 'none');
    $('#list_4').removeClass('d-block');
    $('#spn4').text('+');    
});
$('a#translate_ru').click(function(){
    // $(document).ready(function(){
    //     $.html5Translate(dict, 'ru');
    // });
    // $('span.change_txt').text('RU');
    // localStorage.setItem('leng', 'ru');
    // $('#change1').css('display', 'none');
    // $('#list_4').removeClass('d-block');
    // $('#spn4').text('+');
    
    $(document).ready(function(){
        alert('Sorry, this page is under development!');
    })
});
var checkleng = localStorage.getItem('leng');

$(window).ready(function(){
    if ( checkleng == 'ru'){
        $('span.change_txt').text('RU');
        $.html5Translate(dict, 'ru');
    }
    else {
        $.html5Translate(dict, 'en');
    }
});