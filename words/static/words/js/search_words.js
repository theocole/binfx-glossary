window.onload = function() {
    var content = [
        { category: 'South America', title: 'Brazil' },
        { category: 'South America', title: 'Peru' },
        { category: 'North America', title: 'Canada' },
        { category: 'Asia', title: 'South Korea' },
        { category: 'Asia', title: 'Japan' },
        { category: 'Asia', title: 'China' },
        { category: 'Europe', title: 'Denmark' },
        { category: 'Europe', title: 'England' },
        { category: 'Europe', title: 'France' },
        { category: 'Europe', title: 'Germany' },
        { category: 'Africa', title: 'Ethiopia' },
        { category: 'Africa', title: 'Nigeria' },
        { category: 'Africa', title: 'Zimbabwe' },
    ];

    $.getJSON('/words', function(result, content) {
        console.log(result.results)
        content = result.results;
    });

    $('.ui.search')
        .search({
            verbose: true,
            type: 'category',
            source: content,
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
}


// TODO: on results click, poll for word and definition
function pollResults() {
    console.log("polling for word...")
}
