'use strict';


/*
* Changes the image to a broken or whole clay based on the status of the checkbox
*/
function registerEventHandlers() {
  console.log('registerEventHandlers ran');
  $(':checkbox').on('change', function() {
    var imagetag = this.id + 'img';
    if(this.checked) {
      $('#' + imagetag).attr('src', wholeClay);
    }
    else{
      $('#' + imagetag).attr('src', brokenClay);
    }
  });
}


/*
* loads up the event handlers on page ready
*/
$(document).ready(registerEventHandlers);
