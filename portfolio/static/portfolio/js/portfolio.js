// changing active class for navigation buttons

$('.portfolio-navigation-button').click( function() {
    $(this).addClass('active').siblings().removeClass('active');
  });