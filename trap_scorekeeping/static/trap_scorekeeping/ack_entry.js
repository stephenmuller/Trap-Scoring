'use strict';

function deleteEntry(url) {
  var token = $('input').val();
  $.ajax({
    url: url,
    type: 'DELETE',
    beforeSend: function(xhr) {
      xhr.setRequestHeader('X-CSRFToken', token);
    }
  });
}

function registerEventHandlers() {
  $('li a').on('click', function(e) {
    e.preventDefault();
    deleteEntry(e.currentTarget.href);
    window.location = window.location;
  });
}

$(document).ready(registerEventHandlers);
