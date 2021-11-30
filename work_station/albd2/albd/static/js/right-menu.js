$(document).ready(function () {
  var trigger = $('.rightMenu'),
      overlay = $('.overlay'),
     isClosed = false;

    trigger.click(function () {
      rightMenu_cross();      
    });

    function rightMenu_cross() {

      if (isClosed == true) {          
        overlay.hide();
        trigger.removeClass('is-open');
        trigger.addClass('is-closed');
        isClosed = false;
      } else {   
        overlay.show();
        trigger.removeClass('is-closed');
        trigger.addClass('is-open');
        isClosed = true;
      }
  }
  
  $('[data-toggle="offcanvas"]').click(function () {
        $('#wrapper').toggleClass('toggled');
  });  
});