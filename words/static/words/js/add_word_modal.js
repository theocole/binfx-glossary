$("#add-word").click(function() {
    $('#add-word-modal')
        .modal('show')
    ;
})
$("#cancel-add").click(function() {
    console.log("closing add word")
    $('#add-word-modal')
        .modal('hide')
    ;
})

$("#add-category").click(function() {
    $('#add-category-modal')
        .modal('show')
    ;
})

$("#cancel-add-category").click(function() {
    console.log("closing add word")
    $('#add-category-modal')
        .modal('hide')
    ;
})
