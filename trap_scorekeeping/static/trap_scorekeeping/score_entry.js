'use strict';

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

$(document).ready(registerEventHandlers);
