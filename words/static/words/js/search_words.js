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
                        .text(result.definition);
                    $("#word-placeholder")
                        .hide()
                    return true;
                }
            });
        console.log("loaded")
    });
});
