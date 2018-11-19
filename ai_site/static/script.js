function deleteModal(event) {
    $('#deleteModalLink').attr("href", $(event.target).data('link'));
}

function deleteWithChildrenModal(event) {
    console.log($(event.target).data('link'));
    console.log($(event.target).data('children-link'));
    $('#deleteOnlyModalLink').attr("href", $(event.target).data('link'));
    $('#deleteChildrenModalLink').attr("href", $(event.target).data('children-link'));
}
