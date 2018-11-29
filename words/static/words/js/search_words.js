$(document).ready(function() {
    var content;
    $.getJSON('/words', function(result) {
        $('.ui.search')
            .search({
                verbose: true,
                type: 'category',
                source: result.results,
                onSelect: function(result, response) {
                    console.log('selection:')
                    console.log(result)
                    $("#word-header")
                        .empty()
                    $("#word-definition")
                        .empty()
                    $("#word-placeholder")
                        .show();
                    $("#word-header")
                        .text(result.title);
                    $("#word-definition")
                        .text(result.category);
                    $("#word-placeholder")
                        .hide()
                    return true;
                }
            });
        console.log("loaded")
    });
});



// TODO: on results click, poll for word and definition
function pollResults() {
    console.log("polling for word...")
}
