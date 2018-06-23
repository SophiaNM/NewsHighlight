$('body')
  .on('click', 'form.fourteen button.btn-search', function(event) {
    event.preventDefault();
    var $input = $('form.fourteen input');
    $input.focus();
    if ($input.val().length() > 0) {
      // submit form
    }
  })
;
