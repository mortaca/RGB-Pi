 /**  
  * AppStation HTML 1.0  
  * Template Scripts
  * Created by WpFreeware Team
  *Author Uri : http://www.wpfreeware.com/

  Custom JS
  
  1. HEADER SLIDER
  2. UP & DOWN SCROLL SMOOTH BTN
  3. TOP FIXED BAR
  4. SMOOTH MENU SCROLLING
  5. MOBILE MENU ACTIVE CLOSE 
  6. GOOGLE MAP
  7. PRELOADER 
  8. WOW SMOOTH ANIMATIN

  
**/

 //for main slider
 jQuery(function($){
  
    /* ----------------------------------------------------------- */
    /*  1.HEADER SLIDER
    /* ----------------------------------------------------------- */

    jQuery('#demo1').skdslider({delay:5000, animationSpeed: 2000,showNextPrev:false,showPlayButton:false,autoSlide:false,animationType:'fading'});
      
      jQuery('#responsive').change(function(){
        $('#responsive_wrapper').width(jQuery(this).val());
      });
      // For fixed top bar
       $(window).scroll(function(){
        if($(window).scrollTop() >100 /*or $(window).height()*/){
          $(".navbar-fixed-top").addClass('past-main');   
        }
      else{
        $(".navbar-fixed-top").removeClass('past-main');
      }
    })
   

  /* ----------------------------------------------------------- */
  /*  2.UP & DOWN SCROLL SMOOTH BTN
  /* ----------------------------------------------------------- */     

    $('#firstTop').on("click",function(){
    var percentage = 100;
    var height = $(document).height();
    var remove = +height / +100 * +percentage;
    var spaceFromTop = +height - +remove;
    $('html,body').animate({ scrollTop: spaceFromTop }, 'slow', function () {});
    });

    $('#secondTop').on("click",function(){
    var percentage = 100;
    var height = $(document).height();
    var remove = +height / +100 * +percentage;
    var spaceFromTop = +height - +remove;
    $('html,body').animate({ scrollTop: spaceFromTop }, 'slow', function () {});
    });

    $('#firstBottom').on("click",function() {
    var window_height = $(window).height();
    var document_height = $(document).height();
    $('html,body').animate({ scrollTop: window_height + document_height }, 'slow', function () {});
    });

    $('#secondBottom').on("click",function() {
    var window_height = $(window).height();
    var document_height = $(document).height();
    $('html,body').animate({ scrollTop: window_height + document_height }, 'slow', function () {});
    });

  
  /* ----------------------------------------------------------- */
  /* 3.TOP FIXED BAR
  /* ----------------------------------------------------------- */   

  //Check to see if the window is top if not then display button
  $(window).scroll(function(){
    if ($(this).scrollTop() > 300) {
      $('.scrollToTop').fadeIn();
    } else {
      $('.scrollToTop').fadeOut();
    }
  });
  
  //Click event to scroll to top
  $('.scrollToTop').click(function(){
    $('html, body').animate({scrollTop : 0},800);
    return false;
  }); 

  
  /* ----------------------------------------------------------- */
  /* 4. SMOOTH MENU SCROLLING
  /* ----------------------------------------------------------- */   

   //MENU SCROLLING WITH ACTIVE ITEM SELECTED

    // Cache selectors
    var lastId,
    topMenu = $("#top-menu"),
    topMenuHeight = topMenu.outerHeight()+10,
    // All list items
    menuItems = topMenu.find("a"),
    // Anchors corresponding to menu items
    scrollItems = menuItems.map(function(){
      var item = $($(this).attr("href"));
      if (item.length) { return item; }
    });

    // Bind click handler to menu items
    // so we can get a fancy scroll animation
    menuItems.click(function(e){
      var href = $(this).attr("href"),
          offsetTop = href === "#" ? 0 : $(href).offset().top-topMenuHeight+1;
      $('html, body').stop().animate({ 
          scrollTop: offsetTop
      }, 900);
      e.preventDefault();
    });

    // Bind to scroll
    $(window).scroll(function(){
     // Get container scroll position
     var fromTop = $(this).scrollTop()+topMenuHeight;
     
     // Get id of current scroll item
     var cur = scrollItems.map(function(){
       if ($(this).offset().top < fromTop)
         return this;
     });
     // Get the id of the current element
     cur = cur[cur.length-1];
     var id = cur && cur.length ? cur[0].id : "";
     
     if (lastId !== id) {
      lastId = id;
      // Set/remove active class
      menuItems.parent().removeClass("active").end().filter("[href=#"+id+"]").parent().addClass("active");
     }           
    })

  /* ----------------------------------------------------------- */
  /*  5. MOBILE MENU ACTIVE CLOSE 
  /* ----------------------------------------------------------- */ 

  $('.navbar-nav').on('click', 'li a', function() {
    $('.in').collapse('hide');
  });  


 
  /* ----------------------------------------------------------- */
  /*  7. PRELOADER 
  /* ----------------------------------------------------------- */ 

    jQuery(window).load(function() { // makes sure the whole site is loaded
      $('#status').fadeOut(); // will first fade out the loading animation
      $('#preloader').delay(100).fadeOut('slow'); // will fade out the white DIV that covers the website.
      $('body').delay(100).css({'overflow':'visible'});
    })

  /* ----------------------------------------------------------- */
  /*  8. WOW SMOOTH ANIMATIN
  /* ----------------------------------------------------------- */

    wow = new WOW(
      {
        animateClass: 'animated',
        offset:       100
      }
    );
    wow.init();
 
  
});
	
 
 


  
 