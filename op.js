$('#op')
// Find all <option> elements, and store their original text in a jQuery data object
.find('option').each(function() {
    $(this).data('text', $(this).text());
})
.end()
// End to return $('#op'), and bind change event
.change(function() {
    var $selOpt = $(this).find('option:selected');

    $selOpt
    // Replace text with abbreviation
    .text($selOpt.attr('data-abbr'))
    // For its siblings, revert to original text
    .siblings().each(function() {
        $(this).text($(this).data('text'));
    });
});