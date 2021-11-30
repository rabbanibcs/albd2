jQuery(document).ready(function ($) {

    /*News Tickers*/
    //$('#newsTicker').vTicker();

    /*Search Box*/
    $('.searchBtn').click(function () {
        $('.searchBox').slideToggle();
    });

    /*All section*/
    $('.allSectionBtn').click(function () {
        $('.allSectionBtn em').toggleClass("addcls");
        $('.allSection').slideToggle();
    });

    var sideslider = $('[data-toggle=collapse-side]');
    var sel = sideslider.attr('data-target');
    var sel2 = sideslider.attr('data-target-2');
    sideslider.click(function (event) {
        $(sel).toggleClass('in');
        $(sel2).toggleClass('out');
    });

    /*Gallery slider*/
    $('.slideGallery').bxSlider({
        slideWidth: 320,
        minSlides: 2,
        maxSlides: 12,
        moveSlides: 1,
        slideMargin: 15,
        pager: false,
        auto: true
    });

    $('.slideGalleryMobile').bxSlider({
        minSlides: 1,
        maxSlides: 12,
        moveSlides: 1,
        pager: false

    });

    $('.videoGalleryMobile').bxSlider({
        minSlides: 1,
        maxSlides: 12,
        moveSlides: 1,
        pager: false
    });

    $('.ss').bxSlider({
        minSlides: 2,
        maxSlides: 12,
        moveSlides: 1,
        pager: false

    });

});

