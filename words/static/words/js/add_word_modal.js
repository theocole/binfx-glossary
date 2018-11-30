$("#add-word").click(function() {
    $('.ui.modal')
        .modal('show')
    ;
})
$("#cancel-add").click(function() {
    console.log("closing add word")
    $('.ui.modal')
        .modal('hide')
    ;
})
