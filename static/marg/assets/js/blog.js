$(document).ready(function () {
  const modal = $('#postModal');
  const form = $('#postForm');

  $('.tag-select').select2({
    tags: true,
    tokenSeparators: [','],
    placeholder: "Select or add tags",
  });

  $('.open-modal-btn').click(function () {
    form[0].reset();                 // native reset clears all inputs
    $('.tag-select').val(null).trigger('change');  // clear select2
    modal.css('display', 'flex');
  });

  $('.cancel-btn').click(function (e) {
    e.preventDefault();
    form[0].reset();
    $('.tag-select').val(null).trigger('change');
    modal.css('display', 'none');
  });

  // Optional: clicking outside modal closes and clears form
  $(window).click(function (e) {
    if ($(e.target).is('#postModal')) {
      form[0].reset();
      $('.tag-select').val(null).trigger('change');
      modal.css('display', 'none');
    }
  });
});
