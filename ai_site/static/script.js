function deleteModal(event) {
    $('#deleteModalLink').attr("href", $(event.target).data('link'));
}

function deleteWithChildrenModal(event) {
    console.log($(event.target).data('link'));
    console.log($(event.target).data('children-link'));
    $('#deleteOnlyModalLink').attr("href", $(event.target).data('link'));
    $('#deleteChildrenModalLink').attr("href", $(event.target).data('children-link'));
}

function filePreview(event) {
    let input = event.target;
    if (input.files && input.files[0]) {
        let reader = new FileReader();
        reader.onload = function (e) {
            $('#preview').show();
            $('#preview').attr('src', e.target.result);
        };
        reader.readAsDataURL(input.files[0]);
    }
}

function multipleFilePreview(event) {
    $('#multiple-preview').text('');
    let input = event.target;
    console.log(input.files);
    if (input.files) {
        let number = input.files.length;
        for (i = 0; i < number; i++) {
            let reader = new FileReader();
            reader.onload = function (e) {
                $($.parseHTML('<img class="list-preview-img">')).attr('src', e.target.result)
                    .appendTo($('#multiple-preview'));
            };
            reader.readAsDataURL(input.files[i]);
        }
    }
}

function sendDelete(event) {
    console.log('in send');
    let xhttp = new XMLHttpRequest();
    let url = $(event.target).data('link');
    console.log(url);
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            console.log("deleted");
            $(event.target).parent().hide();
        }
    };
    xhttp.open('GET', url, true);
    xhttp.send();
}