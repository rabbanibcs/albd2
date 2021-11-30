$('.off-canvas-toggle, .off-canvas-close').on('click', function(event) {
    event.preventDefault();
    $('body').toggleClass('off-canvas-active');
  });


  // ===== Scroll to Top ==== 
  $(window).scroll(function() {
    if ($(this).scrollTop() >= 50) {        // If page is scrolled more than 50px
      $('#return-to-top').fadeIn(200);    // Fade in the arrow
    } else {
      $('#return-to-top').fadeOut(200);   // Else fade out the arrow
    }
  });
  $('#return-to-top').click(function() {      // When arrow is clicked
    $('body,html').animate({
      scrollTop : 0                       // Scroll to top of body
    }, 500);
  });
  
  
  $(document).on('mouseup touchend', function(event) {
    var offCanvas = $('.off-canvas')
    if (!offCanvas.is(event.target) && offCanvas.has(event.target).length === 0) {
      $('body').removeClass('off-canvas-active')
    }
  });