'use strict';


function registerEventHandlers() {
  $('Enter score').on('change', function() {
    $('body').css('background', 'blue');
  });
}


$(document).ready(registerEventHandlers);
